#!/usr/bin/env python 
# FIXME: no matplotlib in python 3 for now
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
    r=abs(random.gauss(0,kRadius))
    
    
  def die(self):
    if (random.random()<Idv.deathcurve[self.age]):
      return True
    return False

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
      self.addidv([i        ][i        ],Idv([1,0,0]))
      self.addidv([kSize-1-i][i        ]=Idv([0,1,0]))
      self.addidv([i        ][kSize-1-i]=Idv([0,0,1]))
  
  def addidv(self,xy,idv):
    self.array[xy[0]][xy[1]]=idv
    self.idvl.append(xy)
  
  def removeidv(self,xy):
    self.array[xy[0]][xy[1]]=idv
    self.idvl.append(xy)
  
  
  def tick(self):
    nl=[]
    for idv in self.idvl:
      if (not self.array[idv[0]][idv[1]].tick(self.array,self.idvl)):
        self.array[idv[0]][idv[1]]=None
      else:
        nl.append(idv)
        
              
    

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


