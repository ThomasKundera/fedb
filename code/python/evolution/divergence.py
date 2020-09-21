#!/usr/bin/env python 
# FIXME: no matplotlib in python 3 for now

import random
import time
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

# This code is to observe diverging genetic of a population

# size of the world
kSize  =100
kRadius=3

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
  deathcurve=[.1,.1,.2,.3,.4,.5,.6,1] # Likelihood of dying for each age
  def __init__(self,rgb=[0,0,0]):
    self.rgb=RGB(rgb)
    self.age=0
    
  def tick(self):
    if (self.die()): return False
    self.age+=1
    return True
    
  def die(self):
    if (random.random()<Idv.deathcurve[self.age]):
      return True
    return False
  
  def mate(self,other):
    self.age=0
    self.rgb=RGB([(self.rgb.rgb[i]+other.rgb.rgb[i])/2 for i in range(3)])
    return self
  
  

class WorldMap:
  def __init__(self):
    self.array=[]
    self.xyl=[]
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
    for i in range(10):
      self.addidv([        i,        i],Idv([1,0,0]))
      self.addidv([kSize-1-i,        i],Idv([0,1,0]))
      self.addidv([        i,kSize-1-i],Idv([0,0,1]))
  
  def addidv(self,xy,idv):
    self.array[xy[0]][xy[1]]=idv
    self.xyl.append(xy)
  
  def removeidv(self,xy):
    self.array[xy[0]][xy[1]]=idv
    self.xyl.append(xy)
  
  def safeexists(self,ix,iy):
    if (ix<0 or iy<0 or (ix > kSize) or (iy > kSize)): return False
    return (self.array[ix][iy])

  def isempty(self,ix,iy):
    if (ix<0 or iy<0 or (ix > kSize) or (iy > kSize)): return False
    return (not self.array[ix][iy])

  def lookformate(self,xy):
    r=abs(random.gauss(0,kRadius))
    for ix in range(-int(r)+xy[0],int(r)+xy[0]):
      for iy in range(-int(r)+xy[1],int(r)+xy[1]):
        if (self.safeexists(ix,iy)):
          return [ix,iy]
    return None

  def lookforroom(self,xy):
    r=abs(random.gauss(0,kRadius))
    for ix in range(-int(r)+xy[0],int(r)+xy[0]):
      for iy in range(-int(r)+xy[1],int(r)+xy[1]):
        if (self.isempty(ix,iy)):
          return [ix,iy]
    return None

  
  def tick(self):
    nl=[]
    for xy in self.xyl:
      # Death
      if (self.array[xy[0]][xy[1]]):
        if (not self.array[xy[0]][xy[1]].tick()):
          self.array[xy[0]][xy[1]]=None
          print("death "+str(xy))
        else:
          nl.append(xy)
          xy2=self.lookformate(xy)
          if (xy2):
            xy3=self.lookforroom(xy)
            if (xy3):
              print("heureux evenement "+str(xy3))
              self.array[xy3[0]][xy3[1]]=self.array[xy[0]][xy[1]].mate(self.array[xy2[0]][xy2[1]])
              nl.append(xy3)
    self.xyl=nl
 

    

class World():
  def __init__(self):
    self.wm=WorldMap()

  def tick(self):
    self.wm.tick()

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
    plt.draw()
        
# --------------------------------------------------------------------------
def main():
  w=World()
  for i in range(100):
    print "-----------"
    w.tick()
    w.draw()
    plt.pause(1)

  


# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()


