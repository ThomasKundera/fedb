#!/usr/bin/env python 
# FIXME: no matplotlib in python 3 for now
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

# This code is to observe diverging genetic of a population

# size of the world
kSize=100

# Fixing random state for reproducibility
np.random.seed(19680801)

class RGB:
  def __init__(self,rgb=None):
    if (not rgb):
      self.rgb=[0,0,0]
      return
    self.rgb=rgb
 
  def set(self,rgb=[0,0,0]):
    self.rgb=rgb
    
  def setrandom(self):
    self.rgb=[np.random.random() for _ in range(3)]
    
 
 
class Idv:
  def __init__(self,rgb=[0,0,0]):
    self.rgb=RGB(rgb)
    self.age=0


class WorldMap:
  def __init__(self):
    self.array=[]
    # Zeroing
    for ix in range(kSize):
      ay=[]
      for iy in range(kSize):
        #idv=Idv()
        #idv.rgb.setrandom()
        #ay.append(idv)
        ay.append(None)
      self.array.append(ay)
    # Adding individuals
    self.array[0      ][0      ]=Idv([1,0,0])
    self.array[kSize-1][0      ]=Idv([0,1,0])
    self.array[0      ][kSize-1]=Idv([0,0,1])
    

class World():
  def __init__(self):
    self.wm=WorldMap()

  def draw(self):
    darray=[]
    for ix in range(kSize):
      x=[]
      for iy in range(kSize):
        if (self.wm.array[ix][iy]):
          x.append(self.wm.array[ix][iy].rgb.rgb)
        else:
          x.append([0,0,0])
      darray.append(x)
    plt.imshow(darray)
    plt.show()
        
        
# --------------------------------------------------------------------------
def main():
  w=World()
  w.draw()
  


# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()


