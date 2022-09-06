#!/usr/bin/env python3
import math

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

  def drawCircle(self):
    # Draw them
    fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(10, 4))
    for center_y, center_x, radius in zip(self._cy, self._cx, self._radii):
      print ("( "+str(center_x)+" , "+str(center_y)+" , "+str(radius)+" ) ")
      circy, circx = circle_perimeter(center_y, center_x, radius, shape=self._imgRGB.shape)
      set_color(self._imgRGB, (circy, circx) , [250, 50, 50])

    ax.imshow(self._imgRGB, cmap=plt.cm.gray)
    plt.show()
  
    
  def processCircle(self):
    self.findEdges()
    self.findCircle()


  def processFlatten(self):
    self._flatten_image=0*self._imgRGB
    self._flatten_image=rescale(self._flatten_image,2, multichannel=True)
    cx=self._cx[0]
    cy=self._cy[0]
    r0=self._radii[0]
    
    # FIXME: there is some weird swapping of x/y coordinates
    # we'll deal with it for now.
    ym=cx-r0
    yM=cx+r0
    xm=cy-r0
    xM=cy+r0

    print ("Circle : ( "+str(cx)+" , "+str(cy)+" ) "+str(r0))
    for ix in range(xm,xM):
      for iy in range(ym,yM):
        #print("( "+str(ix)+" , " +str(iy)+" )")
        try:
          color=self._imgRGB[ix,iy]
          print(color)
        except IndexError:
          print("That should not happens: ( "+str(int(ix))+" , " +str(int(iy))+" )")
          continue
        
        r=math.sqrt((cy-ix)*(cy-ix)+(cx-iy)*(cx-iy))
        theta=math.atan2(iy-cx,ix-cy)
        #print ("theta: "+str(theta*180/math.pi)+" x: "+str(ix-cx)+" y: "+str(iy-cy))
        #print ("r0="+str(r0)+" r="+str(r))
        
        try:
          alpha=math.asin(r/r0)
        except ValueError:
          #print("out of the circle: ( "+str(int(ix))+" , " +str(int(iy))+" )")
          continue
        
        #print ("alpha: "+str(alpha*180/math.pi))
        r1=r0*alpha
        
        x=r1*math.cos(theta)+len(self._flatten_image)/2
        y=r1*math.sin(theta)+len(self._flatten_image[0])/2
        
        try:
          self._flatten_image[int(x),int(y)]=color
          #print("In range: ( "+str(int(x))+" , " +str(int(y))+" )")
        except IndexError:
          #print("Out of range: ( "+str(int(x))+" , " +str(int(y))+" )")
    io.imsave("toto.png",self._imgRGB)
    io.imsave("titi.png",self._flatten_image)


  def tester(self):
    for ix in range(xm,xM):
      for iy in range(ym,yM):
        print("( "+str(ix)+" , " +str(iy)+" )")
        try:
          color=self._imgRGB[ix,iy]
          print(color)
        except IndexError:
          print("That should not happens: ( "+str(int(ix))+" , " +str(int(iy))+" )")
          continue
        try:
          self._flatten_image[int(ix),int(iy)]=color
          print("In range: ( "+str(int(ix))+" , " +str(int(iy))+" )")
        except IndexError:
          print("Out of range: ( "+str(int(ix))+" , " +str(int(iy))+" )")
    
    io.imsave("toto.png",self._imgRGB)
    io.imsave("titi.png",self._flatten_image)
         
    
  def drawFlatten(self):
    fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(10, 4))
    ax.imshow(self._flatten_image, cmap=plt.cm.gray)
    plt.show()


def main():
  cl=Clouding("data/EPIC_00000.png",0.05)
  cl.processCircle()
  #cl.drawCircle()
  cl.processFlatten()
  cl.drawFlatten()
  


# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()

