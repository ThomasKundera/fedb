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

from tkunits import km, mm, μm
from tkthread import TkThread
from windmill import Windmill, Wing, FakeWindmill


# Print function with datestamp
def logprint(*args, **kwargs):
    print("[", datetime.datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"), "]", *args, **kwargs)


def fit_horizon(blue_blobs):
    logprint("fit_horizon: Start")
    x = []
    y = []
    for blob in blue_blobs:
        y1, x1, r = blob
        #print(x1, y1)
        x.append(x1)
        y.append(y1)

    z = np.polyfit(x, y, 2)
    model = np.poly1d(z)
    logprint("fit_horizon: End")
    return model


def plot_hsv(hsv_data):
    rgb = hsv_to_rgb(hsv_data)
    plt.imshow(rgb)


def find_blue_blobs(hsv_data):
    logprint("find_blue_blobs: Start")
    hue_data = hsv_data[:, :, 0]
    hue_binary = hue_data > 0.5

    blobs_dog = blob_dog(hue_binary, min_sigma=0.1, threshold=0.1)

    logprint("find_blue_blobs: End")
    return blobs_dog


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
        windmills[m.idx] = m
    logprint("find_windmills_body: End")
    return windmills


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


def fill_fake_windmills(blue_blobs, green_blobs, red_blobs, white_blobs, yellow_blobs):
    logprint("fill_fake_windmills: Start")
    horizon = None
    fakewindmills = []

    for blob in blue_blobs:
        y, x, r = blob
        f = FakeWindmill(horizon, x, y)
        f.set_color('blue')
        fakewindmills.append(f)
    for blob in green_blobs:
        y, x, r = blob
        f = FakeWindmill(horizon, x, y)
        f.set_color('green')
        fakewindmills.append(f)
    for blob in red_blobs:
        y, x, r = blob
        f = FakeWindmill(horizon, x, y)
        f.set_color('red')
        fakewindmills.append(f)
    for blob in white_blobs:
        y, x, r = blob
        f = FakeWindmill(horizon, x, y)
        f.set_color('white')
        fakewindmills.append(f)
    for blob in yellow_blobs:
        y, x, r = blob
        f = FakeWindmill(horizon, x, y)
        f.set_color('yellow')
        fakewindmills.append(f)

    logprint("fill_fake_windmills: End")
    return fakewindmills


def find_windmills(horizon, green_blobs, red_blobs, white_blobs, yellow_blobs):
    logprint("find_windmills: Start")

    windmills = find_windmills_body(
        horizon, red_blobs, white_blobs, yellow_blobs)

    # First time, looking at blobs, then using existing wings
    first_look = True

    wings = {}
    for i in range(3):
        if (first_look):
            for blob in green_blobs:
                y, x, r = blob
                w = Wing(x, y)
                wings[w.idx] = w
                for m in windmills.values():
                    if (m.wing_candidate(w)):
                        w.mill_candidate(m)
            first_look = False
        else:
            for w in wings.values():
                w.possible_mill = []
                for m in windmills.values():
                    if (m.wing_candidate(w)):
                        w.possible_mill.append(m)
        wings = find_wings(windmills, wings)

    fakewindmills = []
    # Add fake windmills from remainig wings locations
    for w in wings.values():
        # print(w.idx)
        f = FakeWindmill(horizon, w.x, w.y)
        f.set_color('purple')
        fakewindmills.append(f)

    print("Windmills: ----------- ")
    for m in windmills.values():
        print(m)
    print("----------------")

    logprint("find_windmills: End")
    return (windmills, fakewindmills)


def find_blobs(hsv_data):
    # Find blobs in parallel
    blue_thread = TkThread(target=find_blue_blobs, args=[hsv_data])
    green_thread = TkThread(target=find_green_blobs, args=[hsv_data])
    red_thread = TkThread(target=find_red_blobs, args=[hsv_data])
    white_thread = TkThread(target=find_white_blobs, args=[hsv_data])
    yellow_thread = TkThread(target=find_yellow_blobs, args=[hsv_data])

    blue_thread.start()
    green_thread.start()
    red_thread.start()
    white_thread.start()
    yellow_thread.start()

    blue_blobs = blue_thread.join()
    green_blobs = green_thread.join()
    red_blobs = red_thread.join()
    white_blobs = white_thread.join()
    yellow_blobs = yellow_thread.join()

    return (blue_blobs, green_blobs, red_blobs, white_blobs, yellow_blobs)


def do_object_identification(imgname):
    logprint("do_object_identification: Start")
    # Open data point image
    data_point_image = plt.imread(os.path.join(
        'data', imgname + '_data.png'))

    # get hue data
    rgb_data = rgba2rgb(data_point_image, background=(0, 0, 0))
    hsv_data = rgb2hsv(rgb_data)
    (blue_blobs, green_blobs, red_blobs, white_blobs,
     yellow_blobs) = find_blobs(hsv_data)

    fakewindmills = fill_fake_windmills(
        blue_blobs, green_blobs, red_blobs, white_blobs, yellow_blobs)

    # fit horizon
    horizon = fit_horizon(blue_blobs)
    #return fakewindmills

    # fit windmills
    (windmills, fakewings) = find_windmills(
        horizon, green_blobs, red_blobs, white_blobs, yellow_blobs)

    logprint("do_object_identification: End")
    return list(windmills.values())+fakewindmills+fakewings


def object_identification(imgname):
    logprint("object_identification: Start")
    # Open original jpeg image
    original_image = plt.imread(os.path.join(
        'data', imgname + '.jpg'))

    # See if we already have data for that image
    pkfile = os.path.join('data', imgname + '.pkl')
    logprint("object_identification: Windmilling")
    if (True and os.path.exists(pkfile)):
        print("Loading windmills from " + pkfile)
        with open(pkfile, 'rb') as f:
            windmills = pickle.load(f)
    else:
        print("Fitting windmills")
        windmills = do_object_identification(imgname)
        with open(pkfile, 'wb') as f:
            pickle.dump(windmills, f)
    logprint("object_identification: Windmilling done")
    return (original_image, windmills)


def draw_scene(original_image, windmills):
    logprint("object_identification: Start")
    # Draw original image
    plt.imshow(original_image)

    # Draw horison
    horizon = windmills[0].horizon
    imglength=original_image.shape[0]
    if (horizon):
        line_x = np.arange(0, imglength)
        line_y = horizon(line_x)
        plt.plot(line_x, line_y)

    # Draw windmills
    for w in windmills:
        w.draw(plt, plt.gca())

    plt.tight_layout()
    plt.show()
    logprint("object_identification: End")


def draw_map(windmills):
    logprint("draw_map: Start")
    m = FakeWindmill(0, 0, 0)
    m.x_simple = 0
    m.y_simple = 0
    m.set_color('red')
    windmills.append(m)
    # Set a grid ccoordinates
    plt.xlim(-1.3, 1.3)
    plt.ylim(0, 46)
    plt.gca().set_aspect('equal', adjustable='box')

    for m in windmills:
        print("( "+str(m.x_simple)+", "+str(m.y_simple)+" )")
        if (not m.fake):
            if (not m.yellow):
                plt.gca().add_patch(plt.Circle((m.x_simple/km, m.y_simple/km), .1, color='blue', fill=True))
            elif (m.beyond_horizon):
                plt.gca().add_patch(plt.Circle((m.x_simple/km, m.y_simple/km), .1, color='blue', fill=True))
            else:
                plt.gca().add_patch(plt.Circle(
                    (m.x_simple/km, m.y_simple/km), .1, color='green', fill=True))
        else:
            plt.gca().add_patch(plt.Circle(
                (m.x_simple/km, m.y_simple/km), .1, color=m.color, fill=True))

    # plt.tight_layout()
    plt.show()
    logprint("draw_map: End")


def find_horizon_distance(windmill):
    logprint("find_horizon_distance: Start")
    hmin = 0
    hmax = 100*km
    for m in windmill:
        if (m.yellow):
            if (m.beyond_horizon):
                hmax = m.distance
            else:
                hmin = m.distance
        print(str(hmin)+" < horizon < "+str(hmax))
    logprint("find_horizon_distance: End")
    return (hmin+hmax)/2


def find_windmill_size(windmill):
    logprint("find_windmill_size: Start")
    yellow_height = 0
    yellow_width = 0
    white_height = 0
    nb = 0
    for m in windmill:
        if (m.yellow):
            if (not m.beyond_horizon):
                yellow_height += m.yellow_height
                yellow_width += m.yellow_width
                white_height += m.white_height
                nb += 1
                print(str(m.yellow_height)+" " +
                      str(m.yellow_width)+" "+str(m.white_height))
    if (nb==0):
        print("No full windmill in scene: Aborting")
        return
    yellow_height = yellow_height/nb
    yellow_width = yellow_width/nb
    white_height = white_height/nb
    print("Mean size: "+str(yellow_height)+" " +
          str(yellow_width)+" "+str(white_height))
    logprint("find_windmill_size: End")


def to_povray(windmills):
    logprint("to_povray: Start")
    f = open(os.path.join("data", "windmill.pov"), "w")

    for m in windmills:
        f.write(m.to_povray())
    f.close()
    logprint("to_povray: End")


def main():
    logprint("main: Start")
    (original_image, windmills) = object_identification(
        "51664909026_2877f487d2_o")
    realmills = [m for m in windmills if not m.fake]
    for m in realmills:
       m.compute_distances()
    find_windmill_size(realmills)
    print(find_horizon_distance(realmills))
    to_povray(realmills)
    draw_scene(original_image, windmills)
    draw_map(realmills)
    logprint("main: End")


# if main call main
if __name__ == "__main__":
    main()
