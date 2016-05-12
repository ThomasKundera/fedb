#!/usr/bin/env python

import sys

import math, random
from datetime import timedelta
import scipy.stats
import matplotlib.pyplot as plt

import point
#import geodesic

kPi=3.141592653

# Distance data: maps.google.fr and distance.to
# Time of flight data: maps.google.fr
#                                             ->       <-   Comp  Actual
#            FROM          TO               H: MN    H: MN   DIST  DIST
kDISTDATA=[["Paris"       ,"London"      , ( 1,10), ( 1,10), 200,  200],
           ["Paris"       ,"Buccuresti"  , ( 2,50), ( 3, 5),1868, 1868],
           ["Paris"       ,"Warsaw"      , ( 2,10), ( 2,20),1368, 1368],
           ["Paris"       ,"Berlin"      , ( 1,35), ( 1,45), 800,  800],
           ["Paris"       ,"Moscow"      , ( 3,25), ( 3,50),2485, 2485],
          #["Paris"       ,"Beijin"      , ( 9,55), (10,55),8217, 8217],
           ["Paris"       ,"HongKong"    , (11,35), (12,50),None, 9615],
           ["Paris"       ,"LosAngeles"  , (11,30), (10,35),None, 9085],
           ["Paris"       ,"Johanesbourg", (10,30), (10,50),None, 8228],
           ["HongKong"    ,"Sydney"      , ( 9,15), ( 8,55),None, 7385],
           ["HongKong"    ,"Johanesbourg", (12,40), (12,50),None,10718],
           ["HongKong"    ,"LosAngeles"  , (13,05), (14,50),None,11647],
           ["Sydney"      ,"LosAngeles"  , (13,40), (14,45),None,12073],
           ["Sydney"      ,"Johanesbourg", (14,20), (11,50),None,11040],
          ]

kDISTDATAtest=[["A"       ,"B"          , ( 1,10), 200],
           ["A"       ,"C"          , ( 1,10), 300],
           ["A"       ,"D"          , ( 1,10),1000],
           ["B"       ,"C"          , ( 1,10), 400],
          ]

class OneFlight:
  def __init__(self,frm,to,dur1,dur2,distance,realdist):
    self._from=frm
    self._to=to
    self._duration=(timedelta(hours=dur1[0],minutes=dur1[1])+timedelta(hours=dur2[0],minutes=dur2[1]))/2
    self._distance=distance
    self._realdist=realdist
    if (self._distance == None):
      self._compdist=True
    else:
      self._compdist=False
    
  def __str__(self):
    s=self._from.ljust(12)+" -> "+self._to.ljust(12)+" : ( "+str(self._duration).ljust(8)+" ) : "
    s+=str(int(self._distance)).rjust(5)
    if (self._compdist):
      s+="* - "
      s+=str(self._realdist).rjust(5)+" ( "+str(int(100.*(self._distance-self._realdist)/self._realdist))+"% )"
    return s

class AllFlights:
  def __init__(self,farray):
    self._flights=[]
    for item in farray:
      of=OneFlight(item[0],item[1],item[2],item[3],item[4],item[5])
      self._flights.append(of)
      
  def __str__(self):
    s="All Flights:\n"
    for of in self._flights:
      s+=str(of)+'\n'
    return s
  
  def find_distance_time_relation(self,display=False):
    x=[]
    y=[]
    for of in self._flights:
      if (of._distance != None):
        x.append(of._duration.total_seconds())
        y.append(of._distance)
    a, b, r_value, p_value, std_err = scipy.stats.linregress(x,y)
    
    self._a=a
    self._b=b
    
    print ("Distante (km) = "+str(a)+" x Temps (secondes) "+str(b)) 
    
    if (display):
      yp=[]
      for xv in x:
        yp.append(a*xv+b)
    
      plt.scatter(x, y  , color='black')
      plt.plot   (x, yp , color='blue',linewidth=3)

      plt.show()
    
  def compute_missing_distances(self):
    for of in self._flights:
      if (of._distance == None):
        of._distance=self._a*of._duration.total_seconds()+self._b

# Looks useless to hide _p here
# but when going sphere, may helps to keep the
# code generic (it is not yet)
class FlatLocation:
  def __init__(self):
    # Random location
    self._p=point.Point((1000*random.random()-500,1000*random.random()-500))

  def __str__(self):
    return str(self._p)

   
  def distance(self,other):
    return self._p.dist(other._p)


class SpherePoint:
  _r=6371
  def __init__(self,theta,phi):
    self._theta=theta
    self._phi=phi
    
  def dist(self,other):
    return geodesic.great_circle_distance(self._r,self._theta,kPi/2-self._phi,other._theta,kPi/2-other._phi)


class GlobeLocation:
  def __init__(self):
    # Random Earth radius:
    #self._r=6751 # Would be nice to deduce it: 10000*random.random()
    # Random location
    self._p=SpherePoint(2*kPi*random.random(),kPi*random.random())
    
  def __str__(self):
    return str(self._p)

  def distance(self,other):
    return self._p.dist(other._p)



class City:
  def __init__(self,name):
    self._name=name
    self._distances={}
    self._loc=FlatLocation()
    #self._loc=GlobeLocation()
    
  def __str__(self):
    return self._name+" "+str(self._loc)
  
  def append_distance(self,ocit,dist):
    if (not self._distances.has_key(ocit)):
      self._distances[ocit]=dist
    else:
      print("WARNING: unexpected duplicated trip: "+str(self)+" "+str(ocit))

  def distance(self,other):
    return self._loc.distance(other._loc)

  def attraction_repulsion(self):
    vtot=point.Point((0,0))
    
    for o,dt in self._distances.items():
      v=o._loc._p-self._loc._p
      d=self._loc.distance(o._loc)
      vtot+=((d-dt)/d)*v
      #print (str(self)+" to "+str(o)+" is currently at "+str(d)
      #                +", but should be at "+str(dt)
      #                +". So moving by "+str(v)+" ( "+str(vtot)+" )")
    self._loc._p+=.1*vtot # why .1 ? dunno


  def chi2(self):
    chi=0
    for c,d in self._distances.items():
      chi += (self.distance(c)-d)*(self.distance(c)-d)
    return chi
           
 
class AllCities:
  def __init__(self,af):
    self._citynames={}
    for of in af._flights:
      if (not self._citynames.has_key(of._from)):
        self._citynames[of._from]=City(of._from)
      if (not self._citynames.has_key(of._to  )):
        self._citynames[of._to  ]=City(of._to  )

    for of in af._flights:
      self._citynames[of._from].append_distance(self._citynames[of._to  ],of._distance)
      # Have to do that too
      self._citynames[of._to  ].append_distance(self._citynames[of._from],of._distance)
    
  def chi2(self):
    chi=0
    for n,c in self._citynames.items():
      chi+=c.chi2()
    return chi

  def attraction_repulsion(self):
    for n,c in self._citynames.items():
      c.attraction_repulsion()
  
  
  def display(self,stop=False):
    x=[]
    y=[]
    n=[]
    for nm,c in self._citynames.items():
      n.append(nm)
      x.append(c._loc._p.x)
      y.append(c._loc._p.y)
      
      plt.annotate(nm, xy = (c._loc._p.x ,c._loc._p.y ))
      
    plt.scatter(x, y  , color='black')
    if (stop):
      plt.show()
    else:
      plt.draw()
    


def main():
  af=AllFlights(kDISTDATA)
  af.find_distance_time_relation(True)
  af.compute_missing_distances()
  print (af)
  sys.exit(0)
  
  ac=AllCities(af)
  chi2=ac.chi2()
  while (chi2>1000):
    print ("Chi2= "+str(chi2))
    #ac.display(True)
    ac.attraction_repulsion()
    chi2=ac.chi2()
  ac.display(True)
  print ("Chi2= "+str(chi2))
  
# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()
