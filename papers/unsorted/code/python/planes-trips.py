#!/usr/bin/env python

import math, random
from datetime import timedelta
import scipy.stats
import numpy # Yes, I know, I should make a choice
import matplotlib.pyplot as plt


kDISTDATA=[["Paris"   ,"London"     , timedelta(hours= 1,minutes=10), 200],
           ["Paris"   ,"Buccuresti" , timedelta(hours= 3,minutes= 5),1868],
           ["Paris"   ,"Warsaw"     , timedelta(hours= 2,minutes=20),1368],
           ["Paris"   ,"Berlin"     , timedelta(hours= 1,minutes=45), 800],
           ["Paris"   ,"Moscow"     , timedelta(hours= 3,minutes=50),2485],
           ["Paris"   ,"HongKong"   , timedelta(hours=12,minutes=50),None],
           ["HongKong","Sydney"     , timedelta(hours= 8,minutes=55),None],
           ["HongKong","LosAngeles" , timedelta(hours=13,minutes=05),None],
           ["Sydney"  ,"LosAngeles" , timedelta(hours=13,minutes=40),None],
          ]


class OneFlight:
  def __init__(self,frm,to,duration,distance=None):
    self._from=frm
    self._to=to
    self._duration=duration
    self._distance=distance

class AllFlights:
  def __init__(self,farray):
    self._flights=[]
    for item in farray:
      of=OneFlight(item[0],item[1],item[2],item[3])
      self._flights.append(of)
      
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

class FlatLocation:
  def __init__(self):
    # Random location
    self._x=1000*random.random()-500
    self._y=1000*random.random()-500
    
  def __str__(self):
    return "( "+str(self._x)+" , "+str(self._y)+" )"

  def distance(self,other):
    return math.sqrt( (self._x-other._x)*(self._x-other._x)
                     +(self._y-other._y)*(self._y-other._y) )


class City:
  def __init__(self,name):
    self._name=name
    self._distances={}
    self._loc=FlatLocation()
    
    
  def __str__(self):
    return self._name
  
  def append_distance(self,ocit,dist):
    if (not self._distances.has_key(ocit)):
      self._distances[ocit]=dist
    else:
      print("WARNING: unexpected duplicated trip: "+str(self)+" "+str(ocit))

  def distance(self,other):
    return self._loc.distance(other._loc)


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
      # Dont do that
      #self._citynames[of._to  ].append_distance(self._citynames[of._from],of._distance)
    
  def chi2(self):
    chi=0
    for n,c in self._citynames.items():
      chi+=c.chi2()
    return chi

  def attraction_repulsion(self):
    pass
  
  
  def display(self):
    x=[]
    y=[]
    n=[]
    for nm,c in self._citynames.items():
      n.append(nm)
      x.append(c._loc._x)
      y.append(c._loc._y)
      
      plt.annotate(nm, xy = (c._loc._x,c._loc._y ))
      
    plt.scatter(x, y  , color='black')

    plt.show()
    


def main():
  af=AllFlights(kDISTDATA)
  af.find_distance_time_relation()
  af.compute_missing_distances()

  ac=AllCities(af)
  ac.display()
  
  

# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()
