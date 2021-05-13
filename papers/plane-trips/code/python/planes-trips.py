#!/usr/bin/env python3

import sys

import math, random
from datetime import timedelta
import scipy.stats
import matplotlib.pyplot as plt

import point
#import geodesic

# London Paris Moscow Berlin Edinburg Buccharest Minsk
# Madrid Amsterdam Istambul Praha Rome
# New-York San-Francisco

# Minsk replaced by Budapest: more filghts there.

# Distance data: distancefromto.net
# Time of flight data: http://www.trvlink.com/download/oneworld/oneworld.pdf
#            FROM          TO                 H: MN    H: MN   DIST  DIST
kDISTDATA=[
           ["London"      ,"Moscow"        , ( 3,45), (4,15),2501, 2501],
           ["London"      ,"Prague"        , ( 2,00), (2,10),1033, 1033],
           ["London"      ,"Madrid"        , ( 2,20), (2,20),1263, 1263],
           ["London"      ,"Buccharest"    , ( 3,15), (3,35),2091, 2091],
           ["London"      ,"Rome"          , ( 2,25), (2,40),1434, 1434],
           ["London"      ,"Budapest"      , ( 2,20), (2,30),1449, 1449],

           ["Paris"       ,"Madrid"        , ( 1,55), (1,55),1053, 1053],
           ["Paris"       ,"Budapest"      , ( 2,15), (2,20),1244, 1244],

           ["Berlin"      ,"Madrid"        , ( 3, 5), (2,55),1870, 1870],

           ["Madrid"      ,"Amsterdam"     , ( 2,30), (2,35),1481, 1481],
           ["Madrid"      ,"Budapest"      , ( 3,10), (3,10),1974, 1974],
           ["Istambul"    ,"Madrid"        , ( 3,55), (4,25),2739, 2739],
           
           ["Amsterdam"   ,"Budapest"      , ( 2,00), (2, 5),1146, 1146],
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
    self._dur_to  =timedelta(hours=dur1[0],minutes=dur1[1])
    self._dur_from=timedelta(hours=dur2[0],minutes=dur2[1])
    self._duration=(self._dur_to+self._dur_from)/2
    self._distance=distance
    self._realdist=realdist
    if (self._distance == None):
      self._compdist=True
    else:
      self._compdist=False
    
  def __str__(self):
    return self.csvstr()
    s=self._from.ljust(12)+" -> "+self._to.ljust(12)+" : ( "+str(self._duration).rjust(8)
    s+=" ("+str(self._dur_to).rjust(8)+" - "+ str(self._dur_from).rjust(8)+" ) "
    s+=" ) : "
    s+=str(int(self._distance)).rjust(5)
    s+=str(int(self._realdist)).rjust(5)
    if (self._compdist):
      s+="* - "
      s+=str(self._realdist).rjust(5)+" ( "+str(int(100.*(self._distance-self._realdist)/self._realdist))+"% )"
    return s
  
  def csvstr(self):
    s=self._from.ljust(12)+" , "+self._to.ljust(12)
    s+=" , "+str(self._dur_to).rjust(8)+" , "+ str(self._dur_from).rjust(8)+" , "
    s+=str(int(self._distance)).rjust(5)
    return s
  
  def texmacs_string(self,opt=None):
    s ="|<row|<cell|"+self._from+">|<cell|"+self._to+">|<cell|"+str(self._duration)+">|<cell|"
    s+=str(self._dur_to)+">|<cell|"+str(self._dur_from)+">|<cell|"+str(int(self._distance))+">"
    if (opt): s+="|<cell|"+str(int(self._realdist))+">"
    s+=">"
    return s


class AllFlights:
  def __init__(self,farray):
    self._flights=[]
    for item in farray:
      #print (item)
      of=OneFlight(item[0],item[1],item[2],item[3],item[4],item[5])
      #print(of)
      #sys.exit(0)
      self._flights.append(of)
      
  def __str__(self):
    s="All Flights:\n"
    s+="FROM            TO               TIME     (To         From     )         D1       D2 ( Err)\n"
    s+="<cwith|2|2|6|6|cell-halign|r>|"
    s+="<cwith|3|3|6|6|cell-halign|r>|"
    s+="<cwith|4|4|6|6|cell-halign|r>|"
    s+="<cwith|5|5|6|6|cell-halign|r>|"
    s+="<cwith|6|6|6|6|cell-halign|r>|"

    for of in self._flights:
      s+=str(of)+'\n'
    s+="\nD1 : distance (*: computed from time of flight)\n"
    s+="D2 : distance (measured on the globe          )\n"
    s+="Err: Difference between D1 and D2\n"
    return s
  
  def texmacs_string_fit(self):
    s ="<small-table|<tabular|<tformat|<cwith|1|1|1|-1|cell-halign|c>|"
    s+="<cwith|2|2|6|6|cell-halign|r>|"
    s+="<cwith|3|3|6|6|cell-halign|r>|"
    s+="<cwith|4|4|6|6|cell-halign|r>|"
    s+="<cwith|5|5|6|6|cell-halign|r>|"
    s+="<cwith|6|6|6|6|cell-halign|r>|"
    s+="<cwith|1|-1|1|-1|cell-lborder|1px>|<cwith|1|-1|1|-1|cell-rborder|1px>|<cwith|1|-1|1|-1|cell-bborder|1px>|<cwith|1|-1|1|-1|cell-tborder|1px>|"
    s+="<table|"
    s+="<row|<cell|<strong|From>>|<cell|<strong|To>>|<cell|<strong|Time>>"
    s+=    "|<cell|<strong|(to>>|<cell|<strong|from)>>|<cell|<strong|Distance (km)>>>"
    for of in self._flights[:5]:
      s+=of.texmacs_string()
    s+=">>>|>\n\n"
    return s

  def texmacs_string_dists(self):
    s ="<small-table|<tabular|<tformat|<cwith|1|1|1|-1|cell-halign|c>|"
    s+="<cwith|1|-1|1|-1|cell-lborder|1px>|<cwith|1|-1|1|-1|cell-rborder|1px>|<cwith|1|-1|1|-1|cell-bborder|1px>|<cwith|1|-1|1|-1|cell-tborder|1px>|"
    for i in range (2,len(kDISTDATA)+2):
       s+="<cwith|"+str(i)+"|"+str(i)+"|6|6|cell-halign|r>|"
       s+="<cwith|"+str(i)+"|"+str(i)+"|7|7|cell-halign|r>|"
    s+="<table|"
    s+="<row|<cell|<strong|From>>|<cell|<strong|To>>|<cell|<strong|Time>>"
    s+=    "|<cell|<strong|(to>>|<cell|<strong|from)>>|<cell|<strong|D1 (km)>>|<cell|<strong|D2 (km)>>>"
    for of in self._flights:
      s+=of.texmacs_string(1)
    s+=">>>|>\n\n"
    return s

  def write_texmacs_fit(self):
    f=open("fittable.tm","wt")
    s="<TeXmacs|1.99.2>\n\n<style|generic>\n\n<\\body>\n\n"
    f.write(s)
    f.write(self.texmacs_string_fit())
    s="</body>\n"
    f.write(s)
    f.close()
  
  def write_texmacs_dists(self):
    f=open("fittable2.tm","wt")
    s="<TeXmacs|1.99.2>\n\n<style|generic>\n\n<\\body>\n\n"
    f.write(s)
    f.write(self.texmacs_string_dists())
    s="</body>\n"
    f.write(s)
    f.close()
  
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
    
    print ("Distance (km) = "+"{:.2f}".format(a)+" x Time (secondes) "+"{:.0f}".format(b)) 
    self.write_texmacs_fit()
    
    yp=[]
    for xv in x:
      yp.append(a*xv+b)
  
    plt.scatter(x, y  , color='black')
    plt.plot   (x, yp , color='blue',linewidth=3)
    plt.xlabel('Time of flight (s)')
    plt.ylabel('Distance of flight (km)')
    plt.savefig('plane_fit.png')
    
    if (display):
      plt.show()
    
  def compute_missing_distances(self):
    for of in self._flights:
      if (of._distance == None):
        of._distance=self._a*of._duration.total_seconds()+self._b
      else:
        of._distance=self._a*of._duration.total_seconds()+self._b
        
    self.write_texmacs_dists()

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
  af.find_distance_time_relation(False)
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
