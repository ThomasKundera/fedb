#!/usr/bin/env python3

import os, sys

import numpy as np

from matplotlib import pyplot as plt
from matplotlib.colors import hsv_to_rgb

from skimage import data
from skimage.color import rgba2rgb, rgb2hsv, rgb2gray
from skimage.draw import ellipse
from skimage.feature import corner_harris, corner_subpix, corner_peaks, match_template, blob_dog, blob_log, blob_doh
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


def fit_horizon(hue_data):
    blue_data = hue_data > 0.5

    # Extract blue pixels from blue_data as a 2D array
    blue_data_point = np.array(blue_data)

    x = []
    y = []
    for raw in range(len(blue_data_point)):
        for col in range(len(blue_data_point[raw])):
            if (blue_data_point[raw][col] == True):
                x.append(col)
                y.append(raw)

    x = np.array(x)
    y = np.array(y)

    data = np.column_stack((x, y))

    # Fit a line to the data points
    model = LineModelND()
    model.estimate(data)

    # generate coordinates of estimated models
    line_x = np.arange(0, 800)
    line_y = model.predict_y(line_x)

    return line_x, line_y


def plot_hsv(hsv_data):
    rgb = hsv_to_rgb(hsv_data)
    plt.imshow(rgb)
    

def find_windmills(hsv_data):
    windmills = []
    
    # Extract white pixels from hsv_data as a 2D array
    val_data = hsv_data[:, :, 2]
    #plt.imshow(val_data)
    #plt.show()
    val_binary = val_data > 0.1
    #plt.imshow(val_binary, cmap='gray')
    #plt.show()
    #sys.exit(0)
    sat_data = hsv_data[:, :, 1]
    #plt.imshow(sat_data)
    #plt.show()
    sat_binary = sat_data < 0.9
    #plt.imshow(sat_binary, cmap='gray')
    #plt.show()
    #sys.exit(0)

    white_data = np.logical_and(sat_binary, val_binary)
    
    #plt.imshow(white_data, cmap='gray')
    #plt.show()
    #sys.exit(0)

    blobs_dog = blob_dog(white_data, min_sigma=0.001, threshold=0.0001)

    for blob in blobs_dog:
        print(blob)
        windmills.append(blob)

    return windmills


def object_identification():
    # Open original jpeg image
    original_image = plt.imread(os.path.join(
        'data', '51664909026_2877f487d2_o_detail.jpg'))
    # Open data point image
    data_point_image = plt.imread(os.path.join(
        'data', '51664909026_2877f487d2_o_detail_data.png'))

    # get hue data
    rgb_data = rgba2rgb(data_point_image,background=(0, 0, 0))
    hsv_data = rgb2hsv(rgb_data)

    hue_data = hsv_data[:, :, 0]

    # fit horizon
    line_x, line_y = fit_horizon(hue_data)

    # fit windmills
    windmills = find_windmills(hsv_data)

    # Draw original image
    plt.imshow(original_image)

    # Draw estimated line
    plt.plot(line_x, line_y)

    # Draw windmills
    for blob in windmills:
        y, x, r = blob
        c = plt.Circle((x, y), r, color='red', linewidth=2, fill=False)
        # plot circles
        plt.gcf().gca().add_artist(c)

    plt.tight_layout()
    plt.show()



    plt.show()


def main():
    object_identification()


# if main call main
if __name__ == "__main__":
    main()
