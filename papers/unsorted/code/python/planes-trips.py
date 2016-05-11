#!/usr/bin/env python
from datetime import timedelta

import scipy.stats

import matplotlib.pyplot as plt


kDISTDATA=[["Paris","London"     , timedelta(hours=1,minutes=10), 200],
           ["Paris","Buccuresti" , timedelta(hours=3,minutes= 5),1868],
           ["Paris","Warsaw"     , timedelta(hours=2,minutes=20),1368],
           ["Paris","Berlin"     , timedelta(hours=1,minutes=45), 800],
           ["Paris","Moscow"     , timedelta(hours=3,minutes=50),2485],
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
      
  def find_distance_time_relation(self):
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
    
    yp=[]
    for xv in x:
      yp.append(a*xv+b)
    
    plt.scatter(x, y  , color='black')
    plt.plot   (x, yp , color='blue',linewidth=3)

    #plt.xticks(())
    #plt.yticks(())

    plt.show()

def main():
  af=AllFlights(kDISTDATA)
  af.find_distance_time_relation()
  

  

# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()
