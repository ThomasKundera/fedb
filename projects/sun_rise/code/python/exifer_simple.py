#!/usr/bin/env python3

import math
import datetime
from PIL import Image
from PIL.ExifTags import TAGS

# Print function with datestamp
def logprint(*args, **kwargs):
    print("[", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "]", *args, **kwargs)

class ExifData:
    """Class to handle EXIF data and timestamps."""
    def __init__(self, imgfile):
        self.imgfile = imgfile
        self.exif_data = None
        self.read_exif()
    
    def read_exif(self):
        try:
            self.exif_data = Image.open(self.imgfile)._getexif()
        except Exception as e:
            logprint(f"ERROR: Failed to read EXIF for {self.imgfile}: {e}")
            raise
        if self.exif_data is None:
            logprint(f"WARNING: No EXIF data for {self.imgfile}")
            raise

        # Get datetime
        self.date_time = self.exif_data.get(0x0132)
        if self.date_time:
            try:
                self.date_time = datetime.datetime.strptime(self.date_time, "%Y:%m:%d %H:%M:%S")
                logprint(f"Date and time: {self.date_time}")
            except ValueError:
                logprint(f"WARNING: Invalid DateTime format in {self.imgfile}")
                raise
        else:
            logprint(f"WARNING: No DateTime in EXIF for {self.imgfile}")
            raise

        # Get image size
        self.width, self.height = Image.open(self.imgfile).size

        # Get focal length:
        self.focal_length = self.exif_data.get(0x920a, 0)
        if self.focal_length == 0:
            self.focal_length = 1100  # 1000mm f/10 + 13mm extension.
    
    def px_to_angle(self, r):
        # Canon 550D: Sensor Size 22.3 x 14.9mm
        pxs = 22.3 / self.width
        pys = pxs
        ps = (pxs + pys) / 2
        a = 2 * math.atan2(r * ps, 2 * self.focal_length)  # Diameter in radians
        return a

    def px_to_mn(self, r):
        return 60*math.degrees(self.px_to_angle(r))

    def angle_to_px(self, a):
        """Convert angle  (radians) to pixel size for Canon 550D sensor."""
        pxs = 22.3 / self.width  # Pixel size in mm (x-dimension)
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
    print(exif_data.width)
    print(exif_data.height)
    print(exif_data.date_time)
    print(exif_data.px_to_angle(1))
    print(exif_data.deg_to_px(0.5))
    
if __name__ == '__main__':
    main()