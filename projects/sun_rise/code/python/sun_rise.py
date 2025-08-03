#!/usr/bin/env python3
import os
import datetime
import cv2
import numpy as np


# Print function with datestamp
def logprint(*args, **kwargs):
    print("[", datetime.datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"), "]", *args, **kwargs)

def find_circles(imgfile):
    # Load image
    image = cv2.imread(imgfile, cv2.IMREAD_COLOR)
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
        minRadius=10,  # Minimum circle radius
        maxRadius=60   # Maximum circle radius (0 = no limit)
    )

    # Process detected circles
    if circles is not None:
        int_circles = np.round(circles[0, :]).astype("int")  # Convert to integer
        for (x, y, r) in int_circles:
            # Draw circle and center on the image
            cv2.circle(image, (x, y), r, (0, 255, 0), 2)  # Green circle
            cv2.circle(image, (x, y), 2, (0, 0, 255), 3)  # Red center
            logprint(f"Circle detected at (x: {x}, y: {y}), radius: {r}")

    # Create unique window name based on image filename
    window_name = f"Circles - {os.path.basename(imgfile)}"
    
    # Display image in its own window
    cv2.imshow(window_name, image)
    return circles

class Analysis:
    def __init__(self):
        pass

    def run(self):
        imgdir='data/500_sun'
        for img in os.listdir(imgdir):
            logprint(f"Processing: {img} --------")
            imgfile=os.path.join(imgdir,img)
            find_circles(imgfile)
            return

def main():
    logprint("main: Start")
    an=Analysis()
    an.run()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    logprint("main: End")


# if main call main
if __name__ == "__main__":
    main()
