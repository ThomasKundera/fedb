#!/usr/bin/env python3

import os
from matplotlib import pyplot as plt

import numpy as np

from skimage import data
from skimage.color import rgba2rgb, rgb2hsv
from skimage.draw import ellipse
from skimage.feature import corner_harris, corner_subpix, corner_peaks, match_template
from skimage.measure import LineModelND, ransac
from skimage.transform import warp, AffineTransform

from tkunits import mm, μm

# Captor size
lx = 35.9*mm
ly = 24.0*mm

# Captor pixel size
px = 6240.
py = 4160.

# Captor pixel pitch
dx = lx/px
dy = ly/py

# Assumed square pixel
dxy = (dx+dy)/2.


def object_identification():
    # Open original jpeg image
    original_image = plt.imread(os.path.join('data', '51664909026_2877f487d2_o.jpg'))
    # Open data point image
    data_point_image = plt.imread(os.path.join('data', '51664909026_2877f487d2_o_data_800.png'))

    # select blue pixels only from data imagepoint image
    rgb_data = rgba2rgb(data_point_image)
    hsv_data = rgb2hsv(rgb_data)
    hue_data = hsv_data[:, :, 0]
    blue_data = hue_data > 0.5

    # Extract blue pixels from blue_data as a 2D array
    blue_data_point = np.array(blue_data)

    for raw in range(len(blue_data_point)):
        for col in range(len(blue_data_point[raw])):
            if (blue_data_point[raw][col] == True):
                print (raw, col)

    # Draw blue_data_point_image
    plt.imshow(blue_data, cmap='gray')
    plt.show()



def main():
    object_identification()


# if main call main
if __name__ == "__main__":
    main()
