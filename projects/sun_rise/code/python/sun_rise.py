#!/usr/bin/env python3

import os
import math
import datetime
import glob
import cv2
import numpy as np
from PIL import Image
from PIL.ExifTags import TAGS
from matplotlib import pyplot as plt
import suncalc
import matplotlib.cm as cm

kBatch = "2025_08_22"  # Batch date
kRSD = 500

# EXIF Dictionary
exif_tags = {
    0x010e: "ImageDescription",
    0x010f: "Make",
    0x0110: "Model",
    0x0132: "DateTime",
    0x829a: "ExposureTime",
    0x829d: "FNumber",
    0x8822: "ExposureProgram",
    0x8827: "ISOSpeedRatings",
    0x9000: "ExifVersion",
    0x9204: "ExposureBiasValue",
    0x9209: "Flash",
    0x920a: "FocalLength",
    0xa002: "PixelXDimension",
    0xa003: "PixelYDimension",
}

# Print function with datestamp
def logprint(*args, **kwargs):
    print("[", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "]", *args, **kwargs)

def adjust_contrast(image, saturation_percentile=99):
    """
    Adjust image contrast to ensure ~1% of pixels saturate (255) in at least one channel.
    
    :param image: Input BGR image (from cv2.imread).
    :param saturation_percentile: Percentile to map to 255 (default: 99 for 1% saturation).
    :return: Contrast-adjusted image.
    """
    # Convert image to float32 for precise calculations
    img_float = image.astype(np.float32)
    
    # Compute the 99th percentile across all channels
    percentile_value = np.percentile(img_float, saturation_percentile, axis=(0, 1))
    
    # Scale each channel so the 99th percentile maps to 255
    for channel in range(3):  # R, G, B
        if percentile_value[channel] > 0:  # Avoid division by zero
            scale = 255.0 / percentile_value[channel]
            img_float[:, :, channel] *= scale
    
    # Clip to [0, 255] and convert back to uint8
    img_adjusted = np.clip(img_float, 0, 255).astype(np.uint8)
    
    return img_adjusted


def find_circles(imgfile, minradius, maxradius):
    print(f"find_circles({imgfile}, {minradius}, {maxradius})")
    image = cv2.imread(imgfile, cv2.IMREAD_COLOR)
    if image is None:
        logprint(f"ERROR: Cannot load image {imgfile}")
        return None, None, None
    #image = adjust_contrast(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_blurred = cv2.medianBlur(gray, 5)
    circles = cv2.HoughCircles(
        gray_blurred,
        cv2.HOUGH_GRADIENT_ALT,
        dp=1,
        minDist=50,
        param1=150,
        param2=0.7,
        minRadius=minradius,
        maxRadius=maxradius
    )
    return circles, image, gray

def check_overexposure(image, gray, x, y, r):
    """Check if >20% of pixels in the Sun disk are overexposed (intensity=255)."""
    # Create a mask for the Sun disk
    h, w = gray.shape
    mask = np.zeros((h, w), dtype=np.uint8)
    cv2.circle(mask, (int(x), int(y)), int(r), 255, -1)  # Filled circle
    # Get pixels within the disk
    disk_pixels = gray[mask == 255]
    if len(disk_pixels) == 0:
        return False, 0.0
    # Count overexposed pixels (intensity=255 for 8-bit grayscale)
    overexposed_count = np.sum(disk_pixels == 255)
    overexposed_ratio = overexposed_count / len(disk_pixels)
    # Return True if >20% are overexposed
    return overexposed_ratio > 0.2, overexposed_ratio

def get_exif(imgfile):
    try:
        image = Image.open(imgfile)
        exif_data = image._getexif()
        image.close()
    except Exception as e:
        logprint(f"ERROR: Failed to read EXIF for {imgfile}: {e}")
        return None, None

    if exif_data is None:
        logprint(f"WARNING: No EXIF data for {imgfile}")
        return None, None

    date_time = exif_data.get(0x0132)
    if date_time:
        try:
            date_time = datetime.datetime.strptime(date_time, "%Y:%m:%d %H:%M:%S")
            logprint(f"Date and time: {date_time}")
        except ValueError:
            logprint(f"WARNING: Invalid DateTime format in {imgfile}")
            return None, None
    else:
        logprint(f"WARNING: No DateTime in EXIF for {imgfile}")
        return None, None

    focal_length = exif_data.get(0x920a, 0)
    if (focal_length == 0):
        #focal_length = 400  # Manual Kenko lens (400mm f/8)
        #focal_length = 1000  # Manual Russian lens (1000mm f/10)
        # The Russian lens has a 13mm extension ring, thus the focal length is larger.
        focal_length = 1012  # 1000mm f/10 + 13mm extension.
    logprint(f"Focal length: {focal_length} mm")
    return date_time, focal_length

def px_to_angle(r, fl):

    # Canon 550D: Sensor Size 22.3 x 14.9mm
    pxs = 22.3 / kRSD
    pys = pxs
    ps = (pxs + pys) / 2
    a = 2 * math.atan2(r * ps, 2 * fl)  # Diameter in radians
    return a

def angle_to_px(a, fl):
    """Convert angular diameter (radians) to pixel radius for Canon 550D sensor."""
    pxs = 22.3 / kRSD  # Pixel size in mm (x-dimension)
    pys = pxs          # Assume same pixel size for y
    ps = (pxs + pys) / 2  # Average pixel size
    r = (2 * fl * math.tan(a / 2)) / ps  # Pixel radius
    return r

def deg_to_px(a, fl):
    """Convert angular diameter (degrees) to pixel radius for Canon 550D sensor."""
    return angle_to_px(math.radians(a), fl)

def resize_image_for_display(image, max_size=(1000, 1000)):
    """Resize image for display while preserving aspect ratio."""
    h, w = image.shape[:2]
    max_width, max_height = max_size
    scale = min(max_width / w, max_height / h, 1.0)
    if scale < 1.0:
        new_w, new_h = int(w * scale), int(h * scale)
        return cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_AREA), scale
    return image, 1.0

class Analysis:
    def __init__(self):
        self.latitude = 43.7  # Nice, France
        self.longitude = 7.3
        self.imgdir = os.path.join('data', kBatch, str(kRSD) + '_sun')

    def for_one_image(self, img):
        logprint(f"Processing: {img} --------")
        imgfile = os.path.join(self.imgdir, img)
        date_time, focal_length = get_exif(imgfile)
        if date_time is None or focal_length is None:
            return None, None, None, None, None
        fInvalid = False
        minradius = int(deg_to_px(0.2, focal_length))  # Sun is about 0.5 degrees
        maxradius = int(deg_to_px(0.3, focal_length))
        circles, image, gray = find_circles(imgfile, minradius, maxradius)
        if circles is None or image is None:
            logprint(f"WARNING: No circles found in {img}")
            fInvalid = True
        elif len(circles[0]) > 1:
            logprint(f"WARNING: Multiple circles found in {img}")
            fInvalid = True

        # Use subpixel precision for calculations
        if not fInvalid:
            x, y, r = circles[0][0]
            is_overexposed, overexposed_ratio = check_overexposure(image, gray, x, y, r)
            if is_overexposed:
                logprint(f"WARNING: Overexposed Sun disk in {img} ({overexposed_ratio*100:.1f}% pixels at 255)")
                fInvalid = True
            else:
                angle = px_to_angle(r, focal_length)
                angle_mn = 2*angle * 60 * 180 / math.pi  # Arc-minutes for diameter
        if fInvalid:
            x, y, r = 0, 0, 0
            angle_mn = 0

        # Get sunrise and sunset times
        sun_times = suncalc.get_times(date_time, self.latitude, self.longitude)
        sunrise = sun_times['sunrise']
        sunset = sun_times['sunset']

        # Resize image for display
        display_image, scale = resize_image_for_display(image)
        x_display, y_display, r_display = int(x * scale), int(y * scale), int(r * scale)
        print(focal_length)
        focal_length_display = round(focal_length, 1)
        text = f"Fl: {focal_length_display:.1f} mm, Angle: {angle_mn:.1f}'"
        cv2.putText(
            display_image,
            text,
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2,
            cv2.LINE_AA
        )

        # Draw circle and center with scaled values
        cv2.circle(display_image, (x_display, y_display), r_display, (0, 255, 0), 2)
        cv2.circle(display_image, (x_display, y_display), 2, (0, 0, 255), 3)

        # Display image
        window_name = f"Circles - {img}"
        if (fInvalid):
            cv2.imshow(window_name, display_image)
        #cv2.waitKey(0)

        if fInvalid:
            return None, None, None, None, None
        return date_time, angle_mn, sunrise, sunset, focal_length

    def plot(self, data_by_day):
        if not data_by_day:
            logprint("ERROR: No valid data to plot")
            return

        fig, ax = plt.subplots(figsize=(10, 5))

        # Get a colormap for unique colors per day
        cmap = cm.get_cmap('tab10')  # Supports up to 10 days
        colors = [cmap(i / len(data_by_day)) for i in range(len(data_by_day))]

        cidx = 0
        for day, (times, angles, sunrise, sunset, focal_lengths) in data_by_day.items():
            # Sort times within the day
            sorted_day_data = sorted(zip(times, angles), key=lambda x: x[0])
            times_sorted, angles_sorted = zip(*sorted_day_data) if sorted_day_data else ([], [])
            # Convert times to hours
            hours = [t.hour + t.minute / 60 + t.second / 3600 for t in times_sorted]
            # Plot angular sizes
            ax.plot(hours, angles_sorted, marker='o', color=colors[cidx], label=f'Angles {day.strftime("%Y-%m-%d")}')
            # Plot sunrise/sunset as vertical lines (use first entry)
            if sunrise and sunset:  # Check lists are non-empty
                sunrise_hour = sunrise[0].hour + sunrise[0].minute / 60 + sunrise[0].second / 3600
                sunset_hour = sunset[0].hour + sunset[0].minute / 60 + sunset[0].second / 3600
                ax.axvline(sunrise_hour, color=colors[cidx], linestyle='--', alpha=0.5, label=f'Sunrise {day.strftime("%Y-%m-%d")}')
                ax.axvline(sunset_hour, color=colors[cidx], linestyle=':', alpha=0.5, label=f'Sunset {day.strftime("%Y-%m-%d")}')
            cidx += 1

        ax.set_xlabel('Time of Day (hours)')
        ax.set_ylabel('Angular Size (arc-minutes)')
        ax.set_xlim(0, 24)
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.legend(loc='best')

        plt.title('Sun Angular Size and Sunrise/Sunset Times by Day')
        plt.tight_layout()
        plt.savefig("sun_plot.png")
        plt.show()

    def plot_diameter_vs_focal(self, data):
        """Plot Sun apparent diameter vs focal length."""
        if not data:
            logprint("ERROR: No valid data to plot")
            return
        fig, ax = plt.subplots(figsize=(10, 5))
        # Group data by focal length
        data_by_focal = {}
        for date_time, angle_mn, _, _, focal_length in data:
            if not date_time or not focal_length:
                continue
            focal_length = round(focal_length, 1)  # Group by rounded focal length
            if focal_length not in data_by_focal:
                data_by_focal[focal_length] = []
            data_by_focal[focal_length].append(angle_mn)
        # Plot
        cmap = cm.get_cmap('tab10')
        colors = [cmap(i / len(data_by_focal)) for i in range(len(data_by_focal))]
        cidx = 0
        for focal_length, angles in sorted(data_by_focal.items()):
            ax.scatter([focal_length] * len(angles), angles, marker='o', color=colors[cidx], label=f'Fl: {focal_length:.1f} mm')
            cidx += 1
        ax.set_xlabel('Focal Length (mm)')
        ax.set_ylabel('Angular Size (arc-minutes)')
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.legend(loc='best')
        plt.title('Sun Apparent Diameter vs Focal Length')
        plt.tight_layout()
        plt.savefig("sun_diameter_vs_focal.png")
        plt.show()

    def run(self):
        self.imgdir = os.path.join('data', kBatch, str(kRSD) + '_sun')
        data = []
        idx = 0
        for img in sorted(os.listdir(self.imgdir)):
            result = self.for_one_image(img)
            if result:
                data.append(result)
                idx += 1
                # if idx > 3:
                #     break
        # Group data by day for first plot
        data_by_day = {}
        for date_time, angle_mn, sunrise, sunset, focal_length in data:
            if not date_time:
                continue
            day = date_time.date()
            if day not in data_by_day:
                data_by_day[day] = ([], [], [], [], [])
            data_by_day[day][0].append(date_time)
            data_by_day[day][1].append(angle_mn)
            data_by_day[day][2].append(sunrise)
            data_by_day[day][3].append(sunset)
            data_by_day[day][4].append(focal_length)
        self.plot(data_by_day)
        self.plot_diameter_vs_focal(data)

def main():
    logprint("main: Start")
    an = Analysis()
    an.run()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    logprint("main: End")

if __name__ == "__main__":
    main()
