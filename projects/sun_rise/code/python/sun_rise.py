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

def find_circles(imgfile):
    # Load image
    image = cv2.imread(imgfile, cv2.IMREAD_COLOR)
    if image is None:
        logprint(f"ERROR: Cannot load image {imgfile}")
        return None, None

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_blurred = cv2.medianBlur(gray, 5)

    # Detect circles using Hough Circle Transform
    circles = cv2.HoughCircles(
        gray_blurred,
        cv2.HOUGH_GRADIENT_ALT,
        dp=1,  # Inverse ratio of resolution
        minDist=50,  # Minimum distance between circle centers
        param1=300,  # Upper threshold for edge detection
        param2=0.9,  # Threshold for circle detection
        minRadius=10,  # Minimum circle radius
        maxRadius=60   # Maximum circle radius (0 = no limit)
    )
    return circles, image

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
    focal_length = float(focal_length) if focal_length else 500  # Default for manual Tamron
    logprint(f"Focal length: {focal_length} mm")
    return date_time, focal_length

def px_to_angle(r,fl):
    # Canon 550D
    # Sensor Size	22.3 x 14.9mm
    # Pixel Dimensions	5184 x 3456
    #pxs=22.3/5184
    #pys=14.9/3456
    pxs=22.3/500
    pys=pxs
    ps=(pxs+pys)/2
    #print(pxs,pys,ps)
    a=2*math.atan2(r*ps,2*fl)
    return a

class Analysis:
    def __init__(self):
        self.latitude = 43.7  # Nice, France; adjust as needed
        self.longitude = 7.3

    def for_one_image(self, img):
        logprint(f"Processing: {img} --------")
        imgfile = os.path.join('data/500_sun', img)
        date_time, focal_length = get_exif(imgfile)
        if date_time is None or focal_length is None:
            return None, None, None, None

        circles, image = find_circles(imgfile)
        if circles is None or image is None:
            logprint(f"WARNING: No circles found in {img}")
            return None, None, None, None
        if len(circles[0]) > 1:
            logprint(f"WARNING: Multiple circles found in {img}")
            return None, None, None, None

        # Use subpixel precision for calculations
        x, y, r = circles[0][0]  # Float values
        angle = 2 * px_to_angle(r, focal_length)  # Diameter
        angle_mn = 60 * angle * 180 / math.pi

        # Get sunrise and sunset times
        sun_times = suncalc.get_times(date_time, self.latitude, self.longitude)
        sunrise = sun_times['sunrise']
        sunset = sun_times['sunset']

        # Round for display only
        text = f"Fl: {focal_length:.1f} mm, Angle: {angle_mn:.1f}°"
        cv2.putText(
            image,
            text,
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,  # Font scale
            (255, 255, 255),  # White text
            2,  # Thickness
            cv2.LINE_AA  # Anti-aliased line type
        )

        # Draw circle and center with rounded values
        cv2.circle(image, (int(x), int(y)), int(r), (0, 255, 0), 2)
        cv2.circle(image, (int(x), int(y)), 2, (0, 0, 255), 3)

        # Display image
        window_name = f"Circles - {img}"
        cv2.imshow(window_name, image)

        return date_time, angle_mn, sunrise, sunset

    def plot(self, data_by_day):
        if not data_by_day:
            logprint("ERROR: No valid data to plot")
            return

        fig, ax = plt.subplots(figsize=(10, 5))

        # Get a colormap for unique colors per day
        cmap = cm.get_cmap('tab10')  # Supports up to 10 days
        colors = [cmap(i / len(data_by_day)) for i in range(len(data_by_day))]

        cidx=0
        for day in data_by_day:
            (times, angles, sunrise, sunset) = data_by_day[day]
            # Sort times within the day
            sorted_day_data = sorted(zip(times, angles), key=lambda x: x[0])
            times_sorted, angles_sorted = zip(*sorted_day_data) if sorted_day_data else ([], [])
            print (angles_sorted)
            # Convert times to hours
            hours = [t.hour + t.minute / 60 + t.second / 3600 for t in times_sorted]
            # Plot angular sizes
            ax.plot(hours, angles_sorted, marker='o', color=colors[cidx], label=f'Angles {day.strftime("%Y-%m-%d")}')
            cidx+=1

        ax.set_xlabel('Time of Day (hours)')
        ax.set_ylabel('Angular Size (degrees)')
        ax.set_xlim(20.5, 21.5)
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.legend(loc='best')

        plt.title('Sun Angular Size and Sunrise/Sunset Times by Day')
        plt.tight_layout()
        plt.savefig("sun_plot.png")
        plt.show()

    def run(self):
        imgdir = 'data/500_sun'
        data = []

        for img in sorted(os.listdir(imgdir)):  # Sort images for consistency
            result = self.for_one_image(img)
            if result:
                data.append(result)

        # Group data by day
        data_by_day = {}
        for date_time, angle_mn, sunrise, sunset in data:
            day = date_time.date()
            if day not in data_by_day:
                data_by_day[day] = ([], [], [], [])
            data_by_day[day][0].append(date_time)  # Times
            data_by_day[day][1].append(angle_mn)   # Angles
            data_by_day[day][2].append(sunrise)    # Sunrise
            data_by_day[day][3].append(sunset)     # Sunset
        #print (data_by_day)
        self.plot(data_by_day)

def main():
    logprint("main: Start")
    an = Analysis()
    an.run()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    logprint("main: End")

if __name__ == "__main__":
    main()
