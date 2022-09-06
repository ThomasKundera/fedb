#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

from skimage import io
from skimage import data, color
from skimage.transform import hough_circle, hough_circle_peaks, rescale
from skimage.feature import canny
from skimage.draw import circle_perimeter, set_color
from skimage.util import img_as_ubyte


# Load picture and detect edges
image0  = io.imread('data/EPIC_00000.png', as_gray=True)
imagergb0 = io.imread('data/EPIC_00000.png')

image = rescale(image0, 0.25, anti_aliasing=False)
imagergb = rescale(imagergb0, 0.25, multichannel=True, anti_aliasing=False)

#image = img_as_ubyte(data.coins()[160:230, 70:270])
edges = canny(image)

# Detect two radii
hough_radii = np.arange(int(0.25*800), int(0.25*1000), 2)
hough_res = hough_circle(edges, hough_radii)

# Select the most prominent 1 circles
accums, cx, cy, radii = hough_circle_peaks(hough_res, hough_radii,total_num_peaks=1)

# Draw them
fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(10, 4))
image = color.gray2rgb(image)
for center_y, center_x, radius in zip(cy, cx, radii):
    print ("( "+str(center_x)+" , "+str(center_y)+" , "+str(radius)+" ) ")
    circy, circx = circle_perimeter(center_y, center_x, radius, shape=imagergb.shape)
    set_color(imagergb, (circy, circx) , [250, 50, 50])

ax.imshow(imagergb, cmap=plt.cm.gray)
plt.show()

