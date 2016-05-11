#!/usr/bin/env python

import math, random
from datetime import timedelta
import scipy.stats
import matplotlib.pyplot as plt

import point

kDISTDATA=[["Paris"   ,"London"     , timedelta(hours= 1,minutes=10), 200],
           ["Paris"   ,"Buccuresti" , timedelta(hours= 3,minutes= 5),1868],
           ["Paris"   ,"Warsaw"     , timedelta(hours= 2,minutes=20),1368],
           ["Paris"   ,"Berlin"     , timedelta(hours= 1,minutes=45), 800],
           ["Paris"   ,"Moscow"     , timedelta(hours= 3,minutes=50),2485],
           ["Paris"   ,"HongKong"   , timedelta(hours=12,minutes=50),None],
           ["Paris"   ,"LosAngeles" , timedelta(hours=10,minutes=35),None],
           ["HongKong","Sydney"     , timedelta(hours= 8,minutes=55),None],
           ["HongKong","LosAngeles" , timedelta(hours=13,minutes=05),None],
           ["Sydney"  ,"LosAngeles" , timedelta(hours=13,minutes=40),None],
          ]

kDISTDATAtest=[["A"       ,"B"          , timedelta(hours= 1,minutes=10), 200],
           ["A"       ,"C"          , timedelta(hours= 1,minutes=10), 300],
           ["A"       ,"D"          , timedelta(hours= 1,minutes=10),1000],
           ["B"       ,"C"          , timedelta(hours= 1,minutes=10), 400],
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
  

class City:
  def __init__(self,name):
    self._name=name
    self._distances={}
    self._loc=FlatLocation()
    
    
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
      d=self._loc._p.dist(o._loc._p)
      vtot+=((d-dt)/d)*v
      print (str(self)+" to "+str(o)+" is currently at "+str(d)
                      +", but should be at "+str(dt)
                      +". So moving by "+str(v)+" ( "+str(vtot)+" )")
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
  af.find_distance_time_relation()
  af.compute_missing_distances()

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
