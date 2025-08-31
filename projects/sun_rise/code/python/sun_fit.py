#!/usr/bin/env python3

import cv2
import numpy as np
import sys

def find_circle(imgfile, min_radius=10, max_radius=50),focal_length=100):
    """
    Fit a circle to the image using HoughCircles with basic Gaussian blur preprocessing.
    
    Args:
        imgfile (str): Path to the image file.r testing).
        min_radius (int): Minimum radius in pixels (default: 10).
        max_radius (int): Maximum radius in pixels (default: 50).
        focal_length (float): Focal length in mm for context (manual fo
    Returns:
        tuple: (image with circle drawn, x, y, r) or (None, None, None, None) if no circle found.
    """
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
        display_image = cv2.cvtColor(gray_blurred, cv2.COLOR_GRAY2BGR)  # Use blurred image for display
        cv2.circle(display_image, (x, y), r, (0, 255, 0), 2)  # Green circle
        cv2.circle(display_image, (x, y), 2, (0, 0, 255), 3)  # Red center

        return display_image, x, y, r
    else:
        print(f"No circles found in {imgfile}")
        return None, None, None, None

def main():
    # Check command-line argument
    if len(sys.argv) != 2:
        print("Usage: python circle_fit_test.py <image_file>")
        sys.exit(1)
    imgfile = sys.argv[1]

    # Manual parameters for self-testing (adjust as needed)
    focal_length = 1012.0  # Example focal length in mm (e.g., Russian lens + 13mm extension)
    min_radius = 15  # Adjusted for ~0.45° diameter at 1012mm
    max_radius = 25  # Adjusted for ~0.55° diameter at 1012mm

    # Fit circle and display
    display_image, x, y, r = fit_circle(imgfile, focal_length, min_radius, max_radius)
    if display_image is not None:
        cv2.imshow("Circle Fit", display_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
