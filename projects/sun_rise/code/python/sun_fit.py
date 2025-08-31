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

def find_circle(imgfile, min_radius=10, max_radius=50,focal_length=100):
    # Load image
    image = cv2.imread(imgfile)
    if image is None:
        print(f"Error: Cannot load image {imgfile}")
        return None, None, None, None

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

        # Draw the circle and center on the original image (converted to BGR for color)
        display_image, scale = resize_image_for_display(gray)
        display_image = cv2.cvtColor(display_image, cv2.COLOR_GRAY2BGR)
        x_display, y_display, r_display = int(x * scale), int(y * scale), int(r * scale)
        cv2.circle(display_image, (x_display, y_display), int(r_display), (0, 255, 0), 2)  # Green circle
        cv2.circle(display_image, (x_display, y_display), 2, (0, 0, 255), 3)  # Red center

        return display_image, x, y, r
    else:
        print(f"No circles found in {imgfile}")
        return None, None, None, None


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

    # Display the image
    if img is not None:
        cv2.imshow("Circle Fit", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
