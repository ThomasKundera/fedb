#!/usr/bin/env python3
import cv2
import numpy as np

# Load image
image = cv2.imread('data/small_jpg/IMG_6758.JPG', cv2.IMREAD_COLOR)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply blur to reduce noise
gray_blurred = cv2.medianBlur(gray, 5)

# Detect circles using Hough Circle Transform
circles = cv2.HoughCircles(
    gray_blurred,
    cv2.HOUGH_GRADIENT,
    dp=1,  # Inverse ratio of resolution
    minDist=20,  # Minimum distance between circle centers
    param1=50,  # Upper threshold for edge detection
    param2=30,  # Threshold for circle detection
    minRadius=0,  # Minimum circle radius
    maxRadius=0   # Maximum circle radius (0 = no limit)
)

# Process detected circles
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")  # Convert to integer
    for (x, y, r) in circles:
        # Draw circle and center on the image
        cv2.circle(image, (x, y), r, (0, 255, 0), 2)  # Green circle
        cv2.circle(image, (x, y), 2, (0, 0, 255), 3)  # Red center
        print(f"Circle detected at (x: {x}, y: {y}), radius: {r}")

# Display or save the result
cv2.imshow("Detected Circles", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# cv2.imwrite("output.jpg", image)  # Optionally save the output