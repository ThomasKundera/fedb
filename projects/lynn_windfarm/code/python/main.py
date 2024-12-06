#!/usr/bin/env python3

import os
import sys
import pickle
import datetime

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

from windmill import Windmill, Wing, FakeWindmill

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

# Print function with datestamp


def logprint(*args, **kwargs):
    print("[", datetime.datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"), "]", *args, **kwargs)


def fit_horizon(hue_data):
    logprint("fit_horizon: Start")
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
    logprint("fit_horizon: End")
    return model


def plot_hsv(hsv_data):
    rgb = hsv_to_rgb(hsv_data)
    plt.imshow(rgb)


def find_white_blobs(hsv_data):
    logprint("find_white_blobs: Start")
    sat_data = hsv_data[:, :, 1]
    sat_binary = sat_data < 0.9
    val_data = hsv_data[:, :, 2]
    val_binary = val_data > 0.1
    white_data = np.logical_and(sat_binary, val_binary)

    blobs_dog = blob_dog(white_data, min_sigma=0.1, threshold=0.1)

    logprint("find_white_blobs: End")
    return blobs_dog


def find_yellow_blobs(hsv_data):
    logprint("find_yellow_blobs: Start")
    hue_data = hsv_data[:, :, 0]
    hue1_binary = hue_data > .1
    hue2_binary = hue_data < .3
    hue_binary = np.logical_and(hue1_binary, hue2_binary)

    yellow_data = hue_binary
    # plt.imshow(yellow_data, cmap='gray')
    # plt.show()

    blobs_dog = blob_dog(yellow_data, min_sigma=0.1, threshold=0.1)
    logprint("find_yellow_blobs: End")
    return blobs_dog


def find_red_blobs(hsv_data):
    logprint("find_red_blobs: Start")
    hue_data = hsv_data[:, :, 0]
    hue_binary = hue_data == 0
    sat_data = hsv_data[:, :, 1]
    sat_binary = sat_data > 0.1
    red_data = np.logical_and(hue_binary, sat_binary)

    blobs_dog = blob_dog(red_data, min_sigma=1, threshold=0.4, overlap=0.1)

    logprint("find_red_blobs: End")
    return blobs_dog


def find_green_blobs(hsv_data):
    logprint("find_green_blobs: Start")
    hue_data = hsv_data[:, :, 0]
    hue1_binary = hue_data > .2
    hue2_binary = hue_data < .6
    hue_binary = np.logical_and(hue1_binary, hue2_binary)
    green_data = hue_binary

    blobs_dog = blob_dog(green_data, min_sigma=1, threshold=0.1)
    # plt.imshow(green_data, cmap='gray')
    # plt.show()

    logprint("find_green_blobs: End")
    return blobs_dog


def find_windmills_body(horizon, red_blobs, white_blobs, yellow_blobs):
    logprint("find_windmills_body: Start")
    fakewindmills = []
    windmills = {}
    # Looks for red blobs, as being center of rotation of windmill
    for blob in red_blobs:
        y, x, r = blob
        m = Windmill(horizon, x, y)
        # Look for possible bottom of windmill
        for blob in white_blobs:
            y1, x1, r1 = blob
            m.bottom_candidate(x1, y1)
        for blob in yellow_blobs:
            y1, x1, r1 = blob
            m.bottom_candidate_yellow(x1, y1)
            f = FakeWindmill(horizon, x1, y1)
            f.set_color('yellow')
            fakewindmills.append(f)
        windmills[m.idx] = m
    logprint("find_windmills_body: End")
    return (windmills, fakewindmills)


def find_wings(windmills, wings):
    logprint("find_wings: Start")
    wings2 = {}
    for w in wings.values():
        if (len(w.possible_mill) == 1):
            if (len(windmills[w.possible_mill[0].idx].wings) == 0):
                windmills[w.possible_mill[0].idx].add_wing(w)
            else:
                wings2[w.idx] = w
        else:
            wings2[w.idx] = w
    wings = wings2
    wings2 = {}
    for m in windmills.values():
        if (len(m.wings) > 0):
            for w in wings.values():
                if (m.wing_candidate(w)):
                    m.add_wing(w)
                    wings2[w.idx] = w

    for w in wings2.values():
        # If idx exists in wings, pop
        if (w.idx in wings):
            wings.pop(w.idx)

    logprint("find_wings: End")
    return (wings)


def find_windmills(horizon, hsv_data):
    logprint("find_windmills: Start")

    white_blobs = find_white_blobs(hsv_data)
    yellow_blobs = find_yellow_blobs(hsv_data)
    red_blobs = find_red_blobs(hsv_data)
    green_blobs = find_green_blobs(hsv_data)

    (windmills, fakewindmills) = find_windmills_body(
        horizon, red_blobs, white_blobs, yellow_blobs)

    # First time, looking at blobs, then using existing wings
    first_look=True

    wings = {}
    for i in range(2):
        if (first_look):
            for blob in green_blobs:
                y, x, r = blob
                f = FakeWindmill(horizon, x, y)
                f.set_color('green')
                fakewindmills.append(f)
                w = Wing(x, y)
                wings[w.idx] = w
                for m in windmills.values():
                    if (m.wing_candidate(w)):
                        w.mill_candidate(m)
            first_look=False
        else:
            for w in wings.values():
                w.possible_mill = []
                for m in windmills.values():
                    if (m.wing_candidate(w)):
                        w.possible_mill.append(m)
        wings=find_wings(windmills, wings)
    
   # Create fake windmills from remainig wings locations
    for w in wings.values():
        #print(w.idx)
        f = FakeWindmill(horizon, w.x, w.y)
        f.set_color('purple')
        fakewindmills.append(f)

    print("Windmills: ----------- ")
    for m in windmills.values():
        print(m)
    print("----------------")

    logprint("find_windmills: End")
    return list(windmills.values())+fakewindmills


def do_object_identification(imgname):
    logprint("do_object_identification: Start")
    # Open data point image
    data_point_image = plt.imread(os.path.join(
        'data', imgname + '_data.png'))

    # get hue data
    rgb_data = rgba2rgb(data_point_image, background=(0, 0, 0))
    hsv_data = rgb2hsv(rgb_data)

    hue_data = hsv_data[:, :, 0]

    # fit horizon
    horizon = fit_horizon(hue_data)
    # generate coordinates of estimated models
    line_x = np.arange(0, 200)
    line_y = horizon.predict_y(line_x)
    # fit windmills
    windmills = find_windmills(horizon, hsv_data)

    logprint("do_object_identification: End")
    return windmills


def object_identification():
    logprint("object_identification: Start")
    imgname = "51664909026_2877f487d2_o_detail3"
    # Open original jpeg image
    original_image = plt.imread(os.path.join(
        'data', imgname + '.jpg'))

    # See if we already have data for that image
    pkfile = os.path.join('data', imgname + '.pkl')
    logprint("object_identification: Windmilling")
    if (False and os.path.exists(pkfile)):
        print("Loading windmills from " + pkfile)
        with open(pkfile, 'rb') as f:
            windmills = pickle.load(f)
    else:
        print("Fitting windmills")
        windmills = do_object_identification(imgname)
        with open(pkfile, 'wb') as f:
            pickle.dump(windmills, f)
    logprint("object_identification: Windmilling done")

    # Draw original image
    plt.imshow(original_image)

    # Draw estimated line
    # plt.plot(line_x, line_y)

    # Draw windmills
    for w in windmills:
        w.draw(plt, plt.gca())

    plt.tight_layout()
    plt.show()
    logprint("object_identification: End")


def main():
    logprint("main: Start")
    object_identification()
    logprint("main: End")


# if main call main
if __name__ == "__main__":
    main()
