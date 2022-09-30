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
kRadius=4

# Fixing random state for reproducibility
np.random.seed(19680801)

class RGB:
  def __init__(self,rgb=None):
    if (not rgb):
      self.rgb=[0.,0.,0.]
      return
    self.rgb=rgb
 
  def set(self,rgb=[0.,0.,0.]):
    self.rgb=rgb
    
  def setrandom(self):
    self.rgb=[np.random.random() for _ in range(3)]
  
  def rgbsum(self):
    return self.rgb[0]+self.rgb[1]+self.rgb[2]
  
  def dist(self,o):
    return (self.rgb[0]-o.rgb[0]) ** 2 + (self.rgb[1]-o.rgb[1]) ** 2 + (self.rgb[2]-o.rgb[2]) ** 2
 
class Idv:
  #deathcurve=[.1,.1,.2,.3,.4,.5,.6,1] # Likelihood of dying for each age
  deathcurve=[.1,.4,.6,.9,1,1,1,1] # Likelihood of dying for each age
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
  
  # This is by mean
  def mate(self,other):
    # FIXME: add a bit of noise here
    idv=Idv([(self.rgb.rgb[i]+other.rgb.rgb[i])/2 for i in range(3)])
    return idv
  
  # This is closer to how DNA works
  def matehard(self,other):
    idv=Idv([random.choice([self.rgb.rgb[i],other.rgb.rgb[i]]) for i in range(3)])
    if (idv.rgb.rgbsum()==0): # genetic defect: death
      idv.age=7 # Trick
    return idv
  
  # Genetic distance
  def gendist(self,other):
    return(self.rgb.dist(other.rgb))

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
      self.addidv([        i,        i],Idv([1.,0.,0.]))
      self.addidv([kSize/2-i,        i],Idv([0.,1.,0.]))
      self.addidv([        i,kSize/2-i],Idv([0.,0.,1.]))
      #self.addidv([kSize/2-i,kSize/2-i],Idv([1.,1.,1.]))
 
  def addidv(self,xy,idv):
    self.array[xy[0]][xy[1]]=idv
    self.xyl.append(xy)
  
  def removeidv(self,xy):
    self.array[xy[0]][xy[1]]=idv
    self.xyl.append(xy)
  
  
  def loopmap(self,xy):
    return [xy[0] % kSize,xy[1] % kSize]
  
  
  def safeexists(self,ix,iy):
    if (ix<0 or iy<0 or (ix >= kSize) or (iy >= kSize)): return False
    return (self.array[ix][iy])

  def isempty(self,ix,iy):
    if (ix<0 or iy<0 or (ix >= kSize) or (iy >= kSize)): return False
    return (not self.array[ix][iy])

  def lookformatesafe(self,xy):
    r=abs(random.gauss(0,kRadius))
    for ix in range(-int(r)+xy[0],int(r)+xy[0]):
      for iy in range(-int(r)+xy[1],int(r)+xy[1]):
        if (self.safeexists(ix,iy)):
          return [ix,iy]
    return None

  def lookformate(self,xy):
    r=abs(random.gauss(0,kRadius))
    for ix in range(-int(r)+xy[0],int(r)+xy[0]):
      for iy in range(-int(r)+xy[1],int(r)+xy[1]):
        [ixs,iys]=self.loopmap([ix,iy])
        if (self.array[ixs][iys]):
          return [ixs,iys]
    return None

  def lookformateshuffled(self,xy):
    r=abs(random.gauss(0,kRadius))
    ixl=range(-int(r)+xy[0],int(r)+xy[0])
    iyl=range(-int(r)+xy[1],int(r)+xy[1])
    random.shuffle(ixl)
    random.shuffle(iyl)
    for ix in ixl:
      for iy in iyl:
        [ixs,iys]=self.loopmap([ix,iy])
        if (self.array[ixs][iys]):
          return [ixs,iys]
    return None
  
  def lookformateshuffledbiased(self,xy):
    r=abs(random.gauss(0,kRadius))
    ixl=range(-int(r)+xy[0],int(r)+xy[0])
    iyl=range(-int(r)+xy[1],int(r)+xy[1])
    random.shuffle(ixl)
    random.shuffle(iyl)
    candidates=[]
    for ix in ixl:
      for iy in iyl:
        [ixs,iys]=self.loopmap([ix,iy])
        if (self.array[ixs][iys]):
          candidates.append([ixs,iys])
    df=1000. # Large
    nxy=None
    for cxy in candidates:
      d=self.array[xy[0]][xy[1]].gendist(self.array[cxy[0]][cxy[1]])
      if (d<=df):
        df=d
        nxy=cxy
    return nxy
 
  
  def lookforroomsafe(self,xy):
    r=abs(random.gauss(0,kRadius))
    for ix in range(-int(r)+xy[0],int(r)+xy[0]):
      for iy in range(-int(r)+xy[1],int(r)+xy[1]):
        if (self.isempty(ix,iy)):
          return [ix,iy]
    return None

  def lookforroom(self,xy):
    r=abs(random.gauss(0,kRadius))
    for ix in range(-int(r)+xy[0],int(r)+xy[0]):
      for iy in range(-int(r)+xy[1],int(r)+xy[1]):
        [ixs,iys]=self.loopmap([ix,iy])
        if (not self.array[ixs][iys]):
          return [ixs,iys]
    return None
  
  def lookforroomshuffled(self,xy):
    r=abs(random.gauss(0,kRadius))
    ixl=range(-int(r)+xy[0],int(r)+xy[0])
    iyl=range(-int(r)+xy[1],int(r)+xy[1])
    random.shuffle(ixl)
    random.shuffle(iyl)
    for ix in ixl:
      for iy in iyl:
        [ixs,iys]=self.loopmap([ix,iy])
        if (not self.array[ixs][iys]):
          return [ixs,iys]
    return None
  
  def tick(self):
    nl=[]
    for xy in self.xyl:
      # Death
      if (self.array[xy[0]][xy[1]]):
        if (not self.array[xy[0]][xy[1]].tick()):
          self.array[xy[0]][xy[1]]=None
          #print("death "+str(xy))
        else:
          nl.append(xy)
          xy2=self.lookformateshuffledbiased(xy)
          if (xy2):
            xy3=self.lookforroomshuffled(xy)
            if (xy3):
              #print("heureux evenement "+str(xy3))
              self.array[xy3[0]][xy3[1]]=self.array[xy[0]][xy[1]].matehard(self.array[xy2[0]][xy2[1]])
              nl.append(xy3)
    self.xyl=nl
 
  def stats(self):
    r=0.
    g=0.
    b=0.
    rs=0.
    gs=0.
    bs=0.
    s=0.
    for xy in self.xyl:
      if (self.safeexists(xy[0],xy[1])):
        s+=1                          
        rgb=self.array[xy[0]][xy[1]].rgb.rgb
        rs+=rgb[0]
        gs+=rgb[1]
        bs+=rgb[2]
        if ( (rgb[0]==1) and (rgb[1]==0) and (rgb[2]==0)):
          r+=1
        if ( (rgb[0]==0) and (rgb[1]==1) and (rgb[2]==0)):
          g+=1
        if ( (rgb[0]==0) and (rgb[1]==0) and (rgb[2]==1)):
          b+=1
    print ("s: "+str(s)+" r: "+str(r/s)+" g: "+str(g/s)+" b: "+str(b/s)+" rs: "+str(rs/s) +" rg: "+str(gs/s)+" rb: "+str(bs/s))
     

class World():
  def __init__(self):
    self.wm=WorldMap()
    self.draw0()

  def tick(self):
    self.wm.tick()

  def stats(self):
    self.wm.stats()

  def draw0(self):
    darray=[]
    for ix in range(kSize):
      x=[]
      for iy in range(kSize):
        if (self.wm.array[ix][iy]):
          x.append(self.wm.array[ix][iy].rgb.rgb)
        else:
          x.append([0,0,0])
      darray.append(x)
    self.h=plt.imshow(darray)
    plt.draw()
        
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
    self.h.set_data(darray)
    plt.draw()
        
# --------------------------------------------------------------------------
def main():
  w=World()
  for i in range(1000):
    #print "-----------"
    w.tick()
    w.draw()
    w.stats()
    plt.pause(0.003)

  


# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()


