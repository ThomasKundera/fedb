#!/usr/bin/env python3

import math
from math import sqrt, sin, cos, tan, atan2, asin

import os
from threading import Thread
import multiprocessing
import queue

import numpy as np
import matplotlib.pyplot as plt

from skimage import io
from skimage import data, color
from skimage.transform import hough_circle, hough_circle_peaks, rescale
from skimage.feature import canny
from skimage.draw import circle_perimeter, set_color
from skimage.util import img_as_ubyte, img_as_uint


class Clouding:
  def __init__(self,fn,rscl=1,edgrscl=1):
    print("Clouding __init__()")
    self._fn=fn
    self._rescale   =rscl    # Rescale factor. 1 means 100%
    self._edgrescale=edgrscl # Rescale factor for edge and cirle detection
                             # will multiply the image factor.
    
    # Load picture and detect edges
    img0    = io.imread(self._fn, as_gray=True)
    imgRGB0 = io.imread(self._fn)

    self._img    = rescale(img0   , self._rescale, anti_aliasing=True                   )
    self._imgRGB = rescale(imgRGB0, self._rescale, anti_aliasing=True, multichannel=True)
    
  def findEdges(self):
    print("Clouding.findEdges(): START")
    self._edges = canny(rescale(self._img,self._edgrescale, anti_aliasing=True ))
    print("Clouding.findEdges(): END")
    
  def findCircle(self):
    print("Clouding.findCircle(): START")
    # Detect two radii
    hough_radii = np.arange(
      int(self._edgrescale*self._rescale*850), 
      int(self._edgrescale*self._rescale*900), 2)
    hough_res = hough_circle(self._edges, hough_radii)
    # Select the most prominent 1 circles
    # The x/y inversion here seems needed.
    self._accums, self._cy, self._cx, self._radii = hough_circle_peaks(hough_res, hough_radii,total_num_peaks=1)
    # Scaling back. WARNING: works only for one circle
    self._cx   [0]=self._cx   [0]/self._edgrescale
    self._cy   [0]=self._cy   [0]/self._edgrescale
    self._radii[0]=self._radii[0]/self._edgrescale
    print("Clouding.findCircle(): END")

  def addCircle(self):
    print("Clouding.addCircle(): START")
    # Gots lots of problem with this, it seems to blacken the whole image
    # very often. That's why I put copy() everywhere
    # Problem, solved FIXME: remove all that
    self._imgRGBcircle=self._imgRGB.copy()
    for center_y, center_x, radius in zip(self._cy, self._cx, self._radii):
      print ("( "+str(center_x)+" , "+str(center_y)+" , "+str(radius)+" ) ")
      circx, circy = circle_perimeter(center_x, center_y, radius, shape=self._imgRGB.shape)
      self._imgRGBcircle[circx,circy]=(.8, .2, .2)
    print("Clouding.addCircle(): END")
      
    
  def drawCircle(self):
    fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(10, 4))
    for center_y, center_x, radius in zip(self._cy, self._cx, self._radii):
      print ("( "+str(center_x)+" , "+str(center_y)+" , "+str(radius)+" ) ")
      circx, circy = circle_perimeter(center_x, center_y, radius, shape=self._imgRGB.shape)
      set_color(self._imgRGB, (circx, circy) , [250, 50, 50])

    ax.imshow(self._imgRGB, cmap=plt.cm.gray)
    plt.show()
  
    
  def processCircle(self):
    self.findEdges()
    self.findCircle()

  def fakeprocessCircle(self):
    self._cx   =[int(len(self._img   )/2)]
    self._cy   =[int(len(self._img[0])/2)]
    self._radii=[int(len(self._img   )/2.5)]
    print ("( "+str(self._cx[0])+" , "+str(self._cy[0])+" , "+str(self._radii[0])+" ) ")

    
  # Wikipedia c'est la vie!
  # https://en.wikipedia.org/wiki/Orthographic_map_projection#Mathematics
  # And this one:
  # https://en.wikipedia.org/wiki/Equirectangular_projection

  def flat_backward_spherical_color(self,x0,y0):
    # IMG 00290 is reference (as being center)
    # Time computation: the file name contains data
    # it ranges from 0 to 618
    # during a real time of  3:50 p.m. to 8:45 p.m
    # that is 4:55 h:m
    fn=os.path.basename(self._fn)
    n=int(fn.split('_')[1].split('.')[0])
    totalt=4*60+55
    t =math.floor(n*totalt/618)
    t0=math.floor(290*totalt/618)
    # Trying image zero as ref (as there is California for ref):
    t0=0
    rot=2*math.pi*(t-t0)/(24*60)
    
    R =self._radii[0]
    cx=self._cx[0]
    cy=self._cy[0]
    
    x=x0-len(self._flatten_image   )/2
    y=y0-len(self._flatten_image[0])/2
    
    
    # First backward compute which coordinates is image point
    lmd0=0
    phi0=rot
      
    if (0): # Orthographic
      rho=sqrt(x*x+y*y)
      if (rho==0): rho=.0001 # will be enough
      try:
        c =asin(rho/R)
      except ValueError:
        return [0,0,0]
      
      phi=asin(cos(c)*sin(phi0)+(y*sin(c)*cos(phi0))/rho)
      lmd=lmd0+atan2(x*sin(c),rho*cos(c)*cos(phi0)-y*sin(c)*sin(phi0))
    else: # Equirectangular
      lmd=x/(R*cos(phi0))+lmd0
      phi=y/R+phi0
      # If we don't break there, then we get overlaps by cycling trig functions
      if (( math.fabs(lmd)> math.pi/2) or ( math.fabs(phi)> math.pi/2)):
        return [0,0,0]
      
    
    # Then forward compute which color is that point on image
    lmd0=0
    phi0=0
    
    # First ensure the point is in the circle
    x1=R*cos(phi)*sin(lmd-lmd0)
    y1=R*(cos(phi0)*sin(phi)-sin(phi0)*cos(phi)*cos(lmd-lmd0))
    if (sqrt(x1*x1+y1*y1) > R):
      return [0,0,0]
    
    # Then add the offest:
    x1=x1+cx
    y1=y1+cy
    
    try:
      color=self._imgRGB[int(x1),int(y1)]
      if (0): # np.linalg.norm(color) > 0.1 ):
        print("( "+str(x0)+" , "+str(y0)+" ) => ( "+str(x2)+" , "+str(y2)+" ) = ("+str(r0)+" , "+str(theta0*180/math.pi)+") = "+str(color))
      return color
    except IndexError:
      return [0,0,0]
    
    

  def processFlattenBackwardSpherical(self):
    print("Clouding.processFlattenBackwardSpherical(): START")
    self._flatten_image=0*self._imgRGB.copy()
    #self._flatten_image=rescale(self._flatten_image,1.5, multichannel=True)
    
    for ix in range(len(self._flatten_image)):
      for iy in range(len(self._flatten_image[0])):
        self._flatten_image[ix,iy]=self.flat_backward_spherical_color(ix,iy)
        
    print("Clouding.processFlattenBackwardSpherical(): END")

    
  def drawFlatten(self):
    fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(10, 4))
    ax.imshow(self._flatten_image, cmap=plt.cm.gray)
    plt.show()


  def writeImage(self,rep):
    print("Clouding.writeImage(): START")
    fn=os.path.basename(self._fn)
    self.addCircle()
    #io.imsave(os.path.join(rep,"rgb-"+fn),self._imgRGB)
    io.imsave(os.path.join(rep,"circle-"+fn),self._imgRGBcircle)
    io.imsave(os.path.join(rep,"flat-"+fn)  ,self._flatten_image)
    print("Clouding.writeImage(): END")


def run_thread(fn):
  print("Processing "+fn)
  cl=Clouding(fn,0.5,0.5)
  #cl=Clouding(fn,0.05,0.5)
  #cl=Clouding("Happy-Test-Screen-01-825x510s.jpg")
  #cl.fakeprocessCircle()
  cl.processCircle()
  #cl.drawCircle()
  cl.processFlattenBackwardSpherical()
  #cl.drawFlatten()
  cl.writeImage("out")


q = queue.Queue()

def worker(q,i):
    while True:
        item = q.get()
        print(f'Working on {item}')
        run_thread(item)
        print(f'Finished {item}')
        q.task_done()


def main():
  for i in range(8):
    t=multiprocessing.Process(target=worker, args=(q,i,), daemon=True).start()
    t=Thread(target=worker, args=(q,i,), daemon=True).start()
  # Images have been rotated 35.15° to put Poles axis in a vertical plane
  # relative to the image. This will reduce math hairiness later
  for f in os.listdir("../../../data/massaged_epic/"):
    if ("EPIC_" in f):
      f=os.path.join("../../../data/massaged_epic/", f)
      if os.path.isfile(f):
        #run_thread(f)
        q.put(f)
  
  q.join()
  


# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()

