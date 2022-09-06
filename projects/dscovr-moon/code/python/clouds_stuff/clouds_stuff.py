#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

from skimage import io
from skimage import data, color
from skimage.transform import hough_circle, hough_circle_peaks, rescale
from skimage.feature import canny
from skimage.draw import circle_perimeter, set_color
from skimage.util import img_as_ubyte


class Clouding:
  def __init__(self,fn,rscl=1):
    self._fn=fn
    self._rescale=rscl # Rescale factor. 1 means 100%

    # Load picture and detect edges
    img0    = io.imread(self._fn, as_gray=True)
    imgRGB0 = io.imread(self._fn)

    self._img    = rescale(img0   , self._rescale, anti_aliasing=True                   )
    self._imgRGB = rescale(imgRGB0, self._rescale, anti_aliasing=True, multichannel=True)
    
  def findEdges(self):
    self._edges = canny(self._img)
    
  def findCircle(self):
    # Detect two radii
    hough_radii = np.arange(int(self._rescale*800), int(self._rescale*1000), 2)
    hough_res = hough_circle(self._edges, hough_radii)
    # Select the most prominent 1 circles
    self._accums, self._cx, self._cy, self._radii = hough_circle_peaks(hough_res, hough_radii,total_num_peaks=1)

  def draw(self):
    # Draw them
    fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(10, 4))
    for center_y, center_x, radius in zip(self._cy, self._cx, self._radii):
      print ("( "+str(center_x)+" , "+str(center_y)+" , "+str(radius)+" ) ")
      circy, circx = circle_perimeter(center_y, center_x, radius, shape=self._imgRGB.shape)
      set_color(self._imgRGB, (circy, circx) , [250, 50, 50])

    ax.imshow(self._imgRGB, cmap=plt.cm.gray)
    plt.show()
  
    
  
    
  def process(self):
    self.findEdges()
    self.findCircle()
    self.draw()
    


def main():
  cl=Clouding("data/EPIC_00000.png",0.1)
  cl.process()



# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()

