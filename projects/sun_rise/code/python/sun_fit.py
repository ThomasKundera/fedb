#!/usr/bin/env python3

import cv2
import numpy as np
import sys

from exifer_simple import ExifData

def resize_image_for_display(image, max_size=(1000, 1000)):
    """Resize image for display while preserving aspect ratio."""
    h, w = image.shape[:2]
    max_width, max_height = max_size
    scale = min(max_width / w, max_height / h, 1.0)
    if scale < 1.0:
        new_w, new_h = int(w * scale), int(h * scale)
        return cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_AREA), scale
    return image, 1.0

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

def find_circle(imgfile, min_radius=10, max_radius=50,focal_length=100):
    # Load image
    image = cv2.imread(imgfile)
    if image is None:
        print(f"Error: Cannot load image {imgfile}")
        return None, None, None, None

    # Adjust contrast for longer focal lengths (>300mm) to enhance Sun brightness
    if focal_length > 300:
        image = adjust_contrast(image, saturation_percentile=99)

    # Convert to grayscale and apply Gaussian blur
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_blurred = cv2.GaussianBlur(gray, (3, 3), 0)

 
    # Detect circle with HoughCircles
    circles = cv2.HoughCircles(
        gray_blurred,
        cv2.HOUGH_GRADIENT,
        dp=1,
        minDist=60,
        param1=100,
        param2=30,
        minRadius=min_radius,
        maxRadius=max_radius
    )

    # Process and draw the best fit circle
    if circles is not None:
        circles = np.uint16(np.around(circles))
        best_circle = circles[0][0]
        x, y, r = best_circle
        print(f"Circle found: x={x}, y={y}, r={r}, image shape: {gray.shape}, focal_length={focal_length}mm")
    else:
        print(f"No circles found in {imgfile}")
        r=None
    # Draw the circle and center on the original image (converted to BGR for color)
    display_image, scale = resize_image_for_display(gray)
    display_image = cv2.cvtColor(display_image, cv2.COLOR_GRAY2BGR)
    if (r is not None):
        x_display, y_display, r_display = int(x * scale), int(y * scale), int(r * scale)
        cv2.circle(display_image, (x_display, y_display), int(r_display), (0, 255, 0), 2)  # Green circle
        cv2.circle(display_image, (x_display, y_display), 2, (0, 0, 255), 3)  # Red center

    # Display image
    window_name = f"Circles - {imgfile}"
    if (r is None):
        cv2.imshow(window_name, display_image)
        return None, None, None, None
    return display_image, x, y, r

def find_sun(imgfile):
    exif = ExifData(imgfile)
    focal_length = exif.focal_length
    min_radius = int(exif.deg_to_px(0.15))  # Sun is about 0.5 degrees
    max_radius = int(exif.deg_to_px(0.35))
    return exif, find_circle(imgfile, min_radius, max_radius, focal_length)


def main():
    # Check command-line argument
    if len(sys.argv) != 2:
        imgfile = 'data/2025_08_22/full_sun/IMG_1347.JPG'
    else:
        imgfile = sys.argv[1]

    _, (img, x, y, r) = find_sun(imgfile)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
