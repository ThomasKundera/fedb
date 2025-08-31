#!/usr/bin/env python3

import os
import datetime
from PIL import Image
from PIL.ExifTags import TAGS
import piexif
from datetime import timedelta
from collections import defaultdict
from dateutil.parser import parse as dateutilparse

def logprint(*args, **kwargs):
    print("[", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "]", *args, **kwargs)

class ExifHandler:
    """Class to handle EXIF data and timestamps."""
    time_ref = [
        ('IMG_6824.JPG', "2022-05-20 16:43:18 GMT+01:00"),
        ('IMG_6825.JPG', "2022-05-20 16:44:47 GMT+01:00"),
        ('IMG_1448.JPG', "2006-01-06 06:19:23.999 GMT+01:00"),
        ('IMG_1449.JPG', "2006-01-06 06:19:36.999 GMT+01:00"),
        ('IMG_1450.JPG', "2006-01-06 06:19:38.999 GMT+01:00")
    ]
    deltas = {}  # Class variable: dict of camera_model: list of (start_exif_time, end_exif_time, delta)

    def __init__(self, directory, threshold_minutes=5):
        """
        Initialize the ExifHandler.

        :param directory: Base directory containing subdirs like 'data/<some_ref>'.
        :param threshold_minutes: Threshold in minutes to average close references (default: 5).
        """
        self.directory = directory
        self.threshold_minutes = threshold_minutes
        self.process_subdirs()

    def parse_time_ref(self, time_str):
        """Parse human-readable timestamp with timezone (e.g., '2006-01-06 06:19:23.999 GMT+01:00')."""
        try:
            return dateutilparse(time_str)
        except ValueError as e:
            logprint(f"ERROR: Failed to parse timestamp {time_str}: {e}")
            return None

    def process_subdirs(self):
        """Process each subdir's time_ref and compute deltas per camera."""
        refs = []
        for subdir in os.listdir(self.directory):
            subdir_path = os.path.join(self.directory, subdir)
            if os.path.isdir(subdir_path):
                time_ref_dir = os.path.join(subdir_path, 'time_ref')
                if os.path.isdir(time_ref_dir):
                    for filename, time_str in self.time_ref:
                        imgfile = os.path.join(time_ref_dir, filename)
                        if os.path.exists(imgfile):
                            exif_ts = self.get_exif_timestamp(imgfile)
                            provided_ts = self.parse_time_ref(time_str)
                            camera = self.get_camera_key(imgfile)
                            if exif_ts and provided_ts and camera:
                                refs.append((camera, exif_ts, provided_ts))
                            else:
                                logprint(f"WARNING: Skipping invalid ref {imgfile}")

        # Group refs by camera
        refs_by_camera = defaultdict(list)
        for camera, exif_ts, provided_ts in refs:
            refs_by_camera[camera].append((exif_ts, provided_ts))

        # Compute deltas per camera
        for camera in refs_by_camera:
            refs_camera = sorted(refs_by_camera[camera], key=lambda x: x[0])
            # Group close refs
            groups = []
            current_group = [refs_camera[0]]
            for i in range(1, len(refs_camera)):
                prev_exif = current_group[-1][0]
                curr_exif = refs_camera[i][0]
                time_diff = (curr_exif - prev_exif).total_seconds() / 60
                if time_diff < self.threshold_minutes:
                    current_group.append(refs_camera[i])
                else:
                    groups.append(current_group)
                    current_group = [refs_camera[i]]
            if current_group:
                groups.append(current_group)

            # Compute avg for each group
            group_avgs = []
            for group in groups:
                exif_times = [exif for exif, _ in group]
                provided_times = [provided for _, provided in group]
                avg_exif = min(exif_times) + sum((exif - min(exif_times) for exif in exif_times), timedelta()) / len(group)
                avg_provided = min(provided_times) + sum((provided - min(provided_times) for provided in provided_times), timedelta()) / len(group)
                group_avgs.append((avg_exif, avg_provided))

            # Compute deltas and intervals
            deltas_camera = []
            if group_avgs:
                for i in range(len(group_avgs)):
                    avg_exif, avg_provided = group_avgs[i]
                    delta = avg_provided - avg_exif
                    # Check for GPS week rollover (if delta > 7 days, subtract ~19.7 years)
                    if delta > timedelta(days=7):
                        delta -= timedelta(weeks=1024)  # ~19.7 years
                    start = datetime.datetime.min if i == 0 else (group_avgs[i-1][0] + avg_exif) / 2
                    end = datetime.datetime.max if i == len(group_avgs) - 1 else (avg_exif + group_avgs[i+1][0]) / 2
                    deltas_camera.append((start, end, delta))
            self.deltas[camera] = deltas_camera

    def get_exif_timestamp(self, imgfile):
        """Extract timestamp from EXIF and make it timezone-aware (GMT+01:00)."""
        try:
            image = Image.open(imgfile)
            exif_data = image._getexif()
            image.close()
            if exif_data:
                date_time = exif_data.get(0x0132)
                if date_time:
                    naive_dt = datetime.datetime.strptime(date_time, "%Y:%m:%d %H:%M:%S")
                    return naive_dt.replace(tzinfo=datetime.timezone(timedelta(hours=1)))  # GMT+01:00
        except Exception as e:
            logprint(f"ERROR: Failed to read EXIF timestamp for {imgfile}: {e}")
        return None

    def get_camera_key(self, imgfile):
        """Get camera model from EXIF (fallback, since Canon body ID not easily accessible)."""
        try:
            image = Image.open(imgfile)
            exif_data = image._getexif()
            image.close()
            if exif_data:
                return exif_data.get(0x0110, 'Unknown')  # Model (e.g., 'Canon EOS 550D')
        except Exception as e:
            logprint(f"ERROR: Failed to read camera model for {imgfile}: {e}")
        return 'Unknown'

    def get_delta_for_time(self, camera, exif_ts):
        """Find the delta for a given exif_ts and camera."""
        if camera not in self.deltas:
            return timedelta(0)
        for start, end, delta in self.deltas[camera]:
            if start <= exif_ts < end:
                return delta
        return timedelta(0)

    def fix_timestamp(self, imgfile, fix=False):
        """Compute corrected timestamp for an image, and optionally apply it."""
        exif_ts = self.get_exif_timestamp(imgfile)
        if exif_ts is None:
            return None
        camera = self.get_camera_key(imgfile)
        delta = self.get_delta_for_time(camera, exif_ts)
        corrected_ts = exif_ts + delta
        if fix:
            try:
                exif_dict = piexif.load(imgfile)
                new_date_str = corrected_ts.strftime("%Y:%m:%d %H:%M:%S")
                exif_dict['0th'][piexif.ImageIFD.DateTime] = new_date_str
                exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = new_date_str
                exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = new_date_str
                exif_bytes = piexif.dump(exif_dict)
                #piexif.insert(exif_bytes, imgfile) Not actually doing anything to the file
                logprint(f"Fixed timestamp for {imgfile} to {new_date_str}")
            except Exception as e:
                logprint(f"ERROR: Failed to write EXIF for {imgfile}: {e}")
        return (exif_ts, corrected_ts)

    def fix_all_images(self, fix=False):
        """Fix timestamps for all images in subdirs of the directory (not time_ref subdirs)."""
        for subdir in os.listdir(self.directory):
            subdir_path = os.path.join(self.directory, subdir)
            if os.path.isdir(subdir_path):
                img_dir = os.path.join(subdir_path, 'IMG')
                if os.path.isdir(img_dir):
                    for img in sorted(os.listdir(img_dir)):
                        if img.lower().endswith('.jpg'):
                            imgfile = os.path.join(img_dir, img)
                            (exif_ts, corrected_ts) = self.fix_timestamp(imgfile, fix=fix)
                            if corrected_ts:
                                logprint(f"Corrected {imgfile} from {exif_ts} to {corrected_ts}")
     
def main():
    exif_handler = ExifHandler('data')
    exif_handler.fix_all_images(fix=False)
 


if __name__ == '__main__':
    main()