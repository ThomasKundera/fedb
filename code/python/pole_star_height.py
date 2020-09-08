#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, './common')

import math
from tkunits import km, dg, pi, earth_radius

import matplotlib.pyplot
import matplotlib.lines



# City latitudes and distances to north pole
#            Name          Lat       dist
kDISTDATA=[["Ikaluktutiak ", 69.12*dg, 2320*km],
           ["Yellowknife  ", 62.44*dg, 3066*km],
           ["Vancouver    ", 49.25*dg, 4536*km],
           ["San Francisco", 37.77*dg, 5814*km],
           ["El Paso      ", 31.76*dg, 6483*km],
           ["Mexico       ", 19.43*dg, 7856*km],
           ["Tegucigalpa  ", 14.10*dg, 8451*km],
          ]

class DataPoint:
  def __init__(self,t):
    self.name=t[0]
    self.lat =t[1]
    self.dist=t[2]
  def __str__(self):
    return(str(self.name)+"\t  "+str(self.lat*180/pi)+"\t "+str(self.dist/1000.))


class tkline:
  def __init__(self):
    self.p0=[0,0]
    self.p1=[0,0]
  
  def from_dist_angle(self,d,a):
    self.p0=[d/1000000.,0]
    self.p1=[0,d*math.tan(a)/1000000.]
    
  def draw(self,fig):
    return
  def __str__(self):
    return(str(self.p0)+" - "+str(self.p1))

def main():
  dp=[]
  for t in kDISTDATA:
    dp.append(DataPoint(t))
  for d in dp:
    print (str(d)+" "+str((pi/2.-d.lat)*earth_radius/1000.))

def main2():
  dp=[]
  for t in kDISTDATA:
    dp.append(DataPoint(t))
      
  fig = matplotlib.pyplot.figure()
  lns=[]
  for d in dp:
    l=tkline()
    l.from_dist_angle(d.dist,d.lat)
    print(l)
    lns.append(matplotlib.lines.Line2D(l.p0, l.p1, transform=fig.transFigure, figure=fig))
  fig.lines.extend(lns)
  l1 = matplotlib.lines.Line2D([0, 1], [0, 1], transform=fig.transFigure, figure=fig)
  l2 = matplotlib.lines.Line2D([0, 1], [1, 0], transform=fig.transFigure, figure=fig)
  fig.lines.extend([l1,l2])
  matplotlib.pyplot.show()
  
def main1():
  fig = matplotlib.pyplot.figure()
  l1 = matplotlib.lines.Line2D([0, 2], [0, 1], transform=fig.transFigure, figure=fig)
  l2 = matplotlib.lines.Line2D([0, 2], [1, 0], transform=fig.transFigure, figure=fig)
  #l3 = matplotlib.lines.Line2D([4,  8], [6, 3], transform=fig.transFigure, figure=fig)
  fig.lines.extend([[0,0],[3,3]])
  matplotlib.pyplot.show()
# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()


