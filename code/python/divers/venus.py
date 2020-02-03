#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '../common')

import math
from tkunits import km, dg, pi, au, earth_radius
import geom3

import matplotlib.pyplot
import matplotlib.lines

kScaleFactor=1./500.
# Objects 2020/01/30 19:30
#           distance   d/earth     d/sun     Az/hau                       ecl j2000                           ecl d
kobjects= [["Earth"  , 0         , 0.985*au, [[0  ,0 ,0   ],[  0, 0, 0  ]],[[  0, 0, 0  ],[ 0,  0,  0  ]],[[  0, 0, 0  ],[ 0,  0,  0  ]]],
           ["Moon"   , 147189*km , 0.984*au, [[266,50,38.9],[ 31,43,11.9]],[[ 14,14,14.5],[-5,-37,-57.2]],[[ 14,31,21.2],[-5,-37,-54.1]]],
           ["Venus"  , 1.098*au  , 0.722*au, [[245,34,37.9],[ 14,16,12.7]],[[350,10,38.6],[-0,-56,-30.1]],[[350,27,44.7],[-0,-56,-30.9]]],
           ["Sun"    , 0.985*au  , 0       , [[266,50,44.9],[-21,-2,-8.5]],[[310, 2,47.3],[ 0,  0,  2.1]],[[310,19,53.2],[ 0,  0,  4.6]]],                        
          ]

def hms2d(hms):
  return hms[0]+hms[1]/60.+hms[2]/3600.
def hms2r(hms):
  return dg*(hms[0]+hms[1]/60.+hms[2]/3600.)

class sp32: # spherical coordinates, no radius
  def __init__(self,a,e):
    self.a=a
    self.e=e
  
  def __str__(self):
    return "["+str(self.a/dg)+","+str(self.e/dg)+"]"
  
class sp32r: 
  def __init__(self,r,a,e):
    self.r=r
    self.a=a
    self.e=e
  
  def __str__(self):
    return str(self.r/km)+" ["+str(self.a/dg)+","+str(self.e/dg)+"]"


def sp32rtoxy(c):
  # Here we purposely ignore the z coordinate
  return geom3.Vector3(c.r*math.cos(c.a),c.r*math.sin(c.a),0)
  
  

class spaceobject:
  __scale=au/10000.
  def __init__(self,line):
    self.name=line[0]
    self.d2earth=line[1]
    self.d2sun=line[2]
    self.azcd=sp32(hms2r(line[5][0]),hms2r(line[5][1]))
    self.recompute()
    
  def recompute(self):
    #self.azel   =sp32r(self.d2earth,hms2r(line[3][0]),hms2r(line[3][1]))
    #self.azelec2=sp32r(self.d2earth,hms2r(line[4][0]),hms2r(line[4][1]))
    self.razcd=sp32r(self.d2earth,self.azcd.a,self.azcd.e)
    
    self.xy=sp32rtoxy(self.razcd)
    

  def rescale(self,s):
    self.d2earth*=s
    self.recompute()

  def __str__(self):
    s =self.name+" \t: "
    #s+=str(self.d2earth/km)+" "
    #s+=str(self.d2sun  /km)+" "
    #s+=str(self.azel)+ " "
    #s+=str(self.azelec2)+" "
    s+=str(self.razcd)
    s+=str(self.xy)
    return s
  
  def display(self):
    matplotlib.pyplot.annotate(self.name, xy = (self.xy.x/self.__scale,self.xy.y/self.__scale))
    matplotlib.pyplot.scatter(self.xy.x/self.__scale, self.xy.y/self.__scale  , color='black')
  
  def circle(self,r):
    return(matplotlib.pyplot.Circle(self.xy/self.__scale, r, color='b', fill=False))

def self_test():
  sod={}
  for line in kobjects:
    so=spaceobject(line)
    sod[so.name]=so
  for nso,so in sod.items():
    print (so)
    so.display()
  matplotlib.pyplot.show()


def main():
  #self_test()
  #return
  Earth=spaceobject(kobjects[0])
  Moon =spaceobject(kobjects[1])
  Venus=spaceobject(kobjects[2])
  Sun  =spaceobject(kobjects[3])
  Venus.rescale(kScaleFactor)
  Sun.rescale(kScaleFactor)
  sod={Earth.name: Earth,
       Moon.name : Moon,
       Venus.name: Venus,
       Sun.name  : Sun}
  matplotlib.pyplot.axis('equal')
  c=Earth.circle(3)
  ax = matplotlib.pyplot.gca()
  ax.cla() # clear things for fresh plot
  #ax.set_xlim((-.1, .1))
  #ax.set_ylim((-.1, .1))

  for nso,so in sod.items():
    print (so)
    so.display()
  ax.add_artist(c)

  matplotlib.pyplot.show()
  
  
  
  
# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()



