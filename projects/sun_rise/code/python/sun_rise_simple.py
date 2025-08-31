#!/usr/bin/env python3

import sys
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

from astro_data_api import get_sun_diameter
from sun_fit import find_sun

kBatch = "2025_08_22"  # Batch date
kRSD = 1000

disk_counter = 0  # Global counter for disk images

# Print function with datestamp
def logprint(*args, **kwargs):
    print("[", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "]", *args, **kwargs)

class Analysis:
    def __init__(self):
        self.latitude = 43.7  # Nice, France
        self.longitude = 7.3
        self.imgdir = os.path.join('data', kBatch, str(kRSD) + '_sun')
        self.disk_out_dir = os.path.join('data', kBatch, 'disk_out')
        os.makedirs(self.disk_out_dir, exist_ok=True)

    def for_one_image(self, img):
        logprint(f"Processing: {img} --------")
        imgfile = os.path.join(self.imgdir, img)
        exif, (imgp, x, y, r) = find_sun(imgfile)
        #print(x, y, r)
        angle_mn = 2*exif.px_to_mn(r)
        focal_length = exif.focal_length
        # Extract image number from filename (e.g., IMG_1234.JPG -> 1234)
        img_num = img.split('_')[1].split('.')[0] if 'IMG_' in img else 'Unknown'
        return exif.date_time, angle_mn, focal_length, img_num

    def plot(self, data_by_day):
        if not data_by_day:
            logprint("ERROR: No valid data to plot")
            return

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.text(0.5, 0.5, 'Preliminary', fontsize=60, color='gray', alpha=0.5, ha='center', va='center', rotation=30, transform=ax.transAxes)

        # Get a colormap for unique colors per day
        cmap = cm.get_cmap('tab20')  # Supports up to 20 days
        colors = [cmap(i / len(data_by_day)) for i in range(len(data_by_day))]

        cidx = 0

        print(data_by_day)

        for day, (times, angles, focal_lengths, img_nums) in data_by_day.items():
            # Sort times within the day
            sorted_day_data = sorted(zip(times, angles, img_nums), key=lambda x: x[0])
            times_sorted, angles_sorted, img_nums_sorted = zip(*sorted_day_data) if sorted_day_data else ([], [], [])
            # Convert times to hours
            hours = [t.hour + t.minute / 60 + t.second / 3600 for t in times_sorted]
            # Plot angular sizes
            ax.plot(hours, angles_sorted, marker='o', color=colors[cidx], label=f'Angles {day.strftime("%Y-%m-%d")}')
            # Annotate each point with image number
            for h, a, img_num in zip(hours, angles_sorted, img_nums_sorted):
                ax.text(h, a, img_num, fontsize=8, ha='right', va='bottom')
            cidx += 1

        ax.set_xlabel('Time of Day (hours)')
        ax.set_ylabel('Angular Size (arc-minutes)')
        ax.set_xlim(5, 22)
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.legend(loc='best')

        plt.title('Sun Angular Size and Sunrise/Sunset Times by Day')
        plt.tight_layout()
        plt.savefig("sun_plot.png")
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
        for date_time, angle_mn, focal_length, img_num in data:
            if not date_time:
                continue
            day = date_time.date()
            if day not in data_by_day:
                data_by_day[day] = ([], [], [], [])  # Add list for img_num
            data_by_day[day][0].append(date_time)
            data_by_day[day][1].append(angle_mn)
            data_by_day[day][2].append(focal_length)
            data_by_day[day][3].append(img_num)  # Store img_num
        
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
