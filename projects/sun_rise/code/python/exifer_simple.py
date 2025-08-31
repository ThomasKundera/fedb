#!/usr/bin/env python3

import math
from PIL import Image
import piexif

# Print function with datestamp
def logprint(*args, **kwargs):
    print("[", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "]", *args, **kwargs)

class ExifData:
    """Class to handle EXIF data and timestamps."""
    def __init__(self, imgfile):
        self.imgfile = imgfile
        self.exif_dict = None
        self.focal_length = None
        self.read_exif()
    
    def read_exif(self):
        try:
            self.exif_dict = piexif.load(self.imgfile)
        except Exception as e:
            logprint(f"ERROR: Failed to read EXIF for {self.imgfile}: {e}")
            raise
        if self.exif_dict is None:
            logprint(f"WARNING: No EXIF data for {self.imgfile}")
            raise
        if 'Exif' not in self.exif_dict:
            logprint(f"WARNING: No EXIF data for {self.imgfile}")
            raise
        if piexif.ExifIFD.FocalLength not in self.exif_dict['Exif']:
            logprint(f"WARNING: No focal length in EXIF for {self.imgfile}")
            return None

        # Print image size:
        image_width = self.exif_dict['0th'][piexif.ImageIFD.ImageWidth]
        image_height = self.exif_dict['0th'][piexif.ImageIFD.ImageLength]
        logprint(f"Image size: {image_width} x {image_height}")

        self.focal_length = self.exif_dict['Exif'][piexif.ExifIFD.FocalLength][0]

        if self.focal_length == 0:
            self.focal_length = 1012  # 1000mm f/10 + 13mm extension.
    
    def px_to_angle(self, r):
        # Canon 550D: Sensor Size 22.3 x 14.9mm
        pxs = 22.3 / kRSD
        pys = pxs
        ps = (pxs + pys) / 2
        a = 2 * math.atan2(r * ps, 2 * self.focal_length)  # Diameter in radians
        return a

    def angle_to_px(self, a):
        """Convert angle  (radians) to pixel size for Canon 550D sensor."""
        pxs = 22.3 / kRSD  # Pixel size in mm (x-dimension)
        pys = pxs          # Assume same pixel size for y
        ps = (pxs + pys) / 2  # Average pixel size
        r = (2 * self.focal_length * math.tan(a / 2)) / ps  # Pixel radius
        return r

    def deg_to_px(self,a):
        """Convert angular diameter (degrees) to pixel radius for Canon 550D sensor."""
        return self.angle_to_px(math.radians(a))

def main():
    exif_data = ExifData('data/2025_08_22/full_sun/IMG_1451.JPG')
    print(exif_data.focal_length)
    
if __name__ == '__main__':
    main()