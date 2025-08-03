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
        cv2.HOUGH_GRADIENT_ALT,
        dp=1,  # Inverse ratio of resolution
        minDist=50,  # Minimum distance between circle centers
        param1=300,  # Upper threshold for edge detection
        param2=0.9,  # Threshold for circle detection
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
            #logprint(f"Circle detected at (x: {x}, y: {y}), radius: {r}")

    return (circles,image)

def get_exif(imgfile):
    image = Image.open(imgfile)
    exif_data = image._getexif()
    image.close()

    date_time = exif_data.get(0x0132)
    if date_time is not None:
        date_time = datetime.datetime.strptime(date_time, "%Y:%m:%d %H:%M:%S")
        logprint(f"Date and time: {date_time}")
    focal_length = float(exif_data.get(0x920a))
    if (focal_length==0): # This is the manual Tamron 
        focal_length=500
    logprint(f"Focal length: {focal_length} mm")
    return (date_time, focal_length)

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
        pass

    def for_one_image(self, img):
        logprint(f"Processing: {img} --------")
        imgfile=os.path.join('data/500_sun',img)
        (dt,fl)=get_exif(imgfile)
        (circles,image)=find_circles(imgfile)
        if circles is None:
            logprint(f"WARNING: No circles found in {img} --------")
            return
        if len(circles)>1:
            logprint(f"WARNING: Multiple circles found in {img} --------")
            return
        #print (circles)
        (x,y,r)=circles[0][0]
        angle=2*px_to_angle(r,fl) # diameter
        print(60*angle*180/math.pi)
        # Add filename as text at the top of the image
        text = f"Fl: {fl:.1f} mm, Angle: {60*angle*180/math.pi:.1f}°"
        cv2.putText(
            image,
            text,
            (10, 30),  # Position (x, y) from top-left
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,  # Font scale
            (255, 255, 255),  # White text
            2,  # Thickness
            cv2.LINE_AA  # Anti-aliased line type
        )

        # Create unique window name based on image filename
        window_name = f"Circles - {img}"
        # Display image in its own window
        cv2.imshow(window_name, image)
        return (dt,60*angle*180/math.pi)

    def plot(self,dtl,al):
        # Create the plot
        plt.figure(figsize=(10, 5))
        plt.plot(dtl, al, marker='o', linestyle='-', color='b', label='Float Values')

        # Format the x-axis for datetimes
        plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y-%m-%d %H:%M'))
        plt.gca().xaxis.set_major_locator(plt.matplotlib.dates.AutoDateLocator())
        plt.xticks(rotation=45)

        # Add labels and title
        plt.xlabel('DateTime')
        plt.ylabel('Float Values')
        plt.title('Float Values vs. DateTime')
        plt.legend()

        # Adjust layout to prevent label cutoff
        plt.tight_layout()

        # Show the plot
        plt.show()


    def run(self):
        imgdir='data/500_sun'
        idx=0
        dtl=[]
        al=[]
        for img in os.listdir(imgdir):
            (dt,a)=self.for_one_image(img)
            dtl.append(dt)
            al.append(a)
            #return
            idx=idx+1
        
        # Pair dt and fl, sort by dt, then unzip
        sorted_pairs = sorted(zip(dtl, al), key=lambda x: x[0])
        dtl_sorted, al_sorted = zip(*sorted_pairs)
        dtl = list(dtl_sorted)
        al = list(al_sorted)
        self.plot(dtl,al)

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
