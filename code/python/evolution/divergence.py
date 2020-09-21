#!/usr/bin/env python 
# FIXME: no matplotlib in python 3 for now

import random
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

# This code is to observe diverging genetic of a population

# size of the world
kSize  =100
kRadius=1

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
  deathcurve=[.5,.2,.3,.4,.5,.6,.8,1] # Likelihood of dying for each age
  def __init__(self,rgb=[0,0,0]):
    self.rgb=RGB(rgb)
    self.age=0
    
  def tick(self,wm,idvl):
    if (self.die()): return False
    self.age+=1
    
  def die(self):
    if (random.random()<Idv.deathcurve[self.age]):
      return True
    return False
  
  def mate(self,other):
    self.age=0
    self.rgb=[(self.rgb[i]+other+rgb[i])/2 for i in range(3)]
  
  

class WorldMap:
  def __init__(self):
    self.array=[]
    self.idvl=[]
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
    self.idvl.append(xy)
  
  def removeidv(self,xy):
    self.array[xy[0]][xy[1]]=idv
    self.idvl.append(xy)
  
  def safeexist(ix,iy):
    if (ix<0 or iy<0 or ix > kSize or iy > kSize): return False
    return (self.array[ix][iy])

  def lookformate(self,xy):
    r=abs(random.gauss(0,kRadius))
    for ix in range(-int(r)+xy[0],int(r)+xy[0]):
      for iy in range(-int(r)+xy[1],int(r)+xy[1]):
        if (self.safeexists(ix,iy)):
          xym=[(xy[0]+ix)/2,(xy[1]+iy)/2]
          if (not (self.safeexists(xym[0],iym[1]))):
            return [ix,iy]
    return None

  
  def tick(self):
    nl=[]
    for xy in self.idvl:
      # Death
      if (not self.array[xy[0]][xy[1]].tick(self.array,self.idvl)):
        self.array[xy[0]][xy[1]]=None
      else:
        nl.append(idv)
        xy2=self.lookformate(xy)
        if (xy2):
          xym=[(xy[0]+xy2[0])/2,(xy[1]+xy2[1])/2]
          self.array[xym[0]][xym[1]]=self.array[xy[0]][xy[1]].mate(self.array[xy2[0]][xy2[1]])
          nl.append(xym)
    self.idvl=nl
 

    

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
    plt.show()
        
        
# --------------------------------------------------------------------------
def main():
  w=World()
  w.tick()
  w.draw()
  


# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()


