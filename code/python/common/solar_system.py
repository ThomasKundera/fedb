#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import geom3


# Units
# Distance
m=1./1000.
km=1000.*m
ua=149597870700*m
# Time
s=1.
m_t=60.*s
h_t=3600.*s
d_t=24.*h_t
Y=31556925.98*s
# Mass
kg=1.

#derivatives
N=kg*m/(s*s)

# Constants

G=6.67E-11*N*m*m/(kg*kg)

# --------------------------------------------------------------------------
# Wikipedia
# Nom Demi-grand axe(UA) Excentricité Inclinaison(°) Période(Y) Mass(kg) axial tilt, self period, offset

planetsArray=[ 
  ["Mercure" ,  0.38710*ua , 0.205631 ,  7.0049  ,   0.2408 *Y ,  330.2E21*kg ,-1          , 0,                     0],
  ["Vénus"   ,  0.72333*ua , 0.006773 ,  3.3947  ,   0.6152 *Y , 4.8685E24*kg ,-1          , 0,                     0],
  ["Terre"   ,  1.00000*ua , 0.016710 ,  0.00000 ,   1.00000*Y , 5.9736E24*kg , 23.4392811 , 23+h_t+56*m_t+4.084*s, 0],
  ["Mars"    ,  1.52366*ua , 0.093412 ,  1.8506  ,   1.8808 *Y , 641.85E21*kg ,-1          , 0,                     0],
  ["Cérès"   ,  2.7665 *ua , 0.078375 , 10.5834  ,   4.601  *Y ,   9.46E20*kg ,-1          , 0,                     0],
  ["Jupiter" ,  5.20336*ua , 0.048393 ,  1.3053  ,  11.862  *Y , 1.8986E27*kg ,-1          , 0,                     0],
  ["Saturne" ,  9.53707*ua , 0.054151 ,  2.4845  ,  29.457  *Y , 568.46E24*kg ,-1          , 0,                     0],
  ["Uranus"  , 19.1913 *ua , 0.047168 ,  0.7699  ,  84.018  *Y , 8.6810E25*kg ,-1          , 0,                     0],
  ["Neptune" , 30.0690 *ua , 0.008586 ,  1.7692  , 164.78   *Y , 102.43E24*kg ,-1          , 0,                     0],
  ["Pluton"  , 39.4817 *ua , 0.248808 , 17.1417  , 248.4    *Y ,  1.314E22*kg ,-1          , 0,                     0],
  ["Éris"    , 68.1461 *ua , 0.432439 , 43.7408  , 562.55   *Y ,   1.66E22*kg ,-1          , 0,                     0]
]
sunMass=1.9891E30*kg
sunRadius=696340*km
earthRadius=6371.0*km

# Moons

# Earth Moon
# Wikipedia
#             Name  sma      Excentr  inclinaison (° ecliptic) Orbital period, mass, tilt, self period,offset
Earth_Moons=["Moon",384399*km, 0.0549,  0, 27.321661*d_t, 0,0,0,-math.pi]
moonRadius=1737.1*km


# https://stackoverflow.com/questions/20659456/python-implementing-a-numerical-equation-solver-newton-raphson
class NewtonRaphson:
  def __init__(self,f,fp):
    self.f=f
    self.fp=fp
    
  def solve(self,x0,h):
    lastX = x0
    nextX = lastX + 10* h  # "different than lastX so loop starts OK
    while (abs(lastX - nextX) > h):  # this is how you terminate the loop - note use of abs()
        newY = self.f(nextX)                     # just for debug... see what happens
        lastX = nextX
        nextX = lastX - newY / self.fp(lastX)  # update estimate using N-R
    return nextX


class AnomalySolver(NewtonRaphson):
  def __init__(self,e,M):
    self.e=e
    self.M=M
    super(AnomalySolver, self).__init__(self.fa(),self.fap)

  def fa(self,x):
    return x-self.e*math.sin(x)-self.M

  def fap(self,x):
    return 1+self.e*math.cos(x)



class Orbit:
  def __init__(self, sma, excentricity,inclinaison,period,mass,tilt,offset=0):
    self.sma=sma
    self.excentricity=excentricity
    self.inclinaison=inclinaison
    self.period=period
    self.offset=offset
    self.lastlocE=0
    
  def get_location(self,t):
    n=2*math.pi/self.period
    M=n*t
    e=self.excentricity # notation
    ans=AnomalySolver(e,M)
    E=ans.solve(self.lastlocE,0.1)
    self.lastlocE=E
    print (E)
    theta=2*math.atan(math.sqtr((1+e)*(math.tan(E/2))*(math.tan(E/2))/(1-e)))
    print (theta)
    
class SimpleOrbit(Orbit):
  def __init__(self, sma, excentricity,inclinaison,period,mass,tilt,offset=0):
    super(SimpleOrbit, self).__init__(sma,excentricity,inclinaison,period,mass,tilt,offset)
    
  def get_location(self,t):
    #print (self.offset)
    theta=self.offset+t*2*math.pi/self.period
    return geom3.Point3(self.sma*math.cos(theta),self.sma*math.sin(theta),0)

class SpaceObject:
  def __init__(self,name):
    self.name=name
  
  def get_location(self,t):
    return geom3.Point3(0,0,0)
  
  def __str__(self):
    return self.name

class Sun(SpaceObject):
  def __init__(self):
     super(Sun, self).__init__("Sun")


class Satellite(SpaceObject):
  def __init__(self,dataray):
    super(Satellite, self).__init__(dataray[0])
    self.orbit=SimpleOrbit(dataray[1],dataray[2],dataray[3],dataray[4],dataray[5],dataray[6],dataray[8])

  def attach_to(self,p):
    self.planet=p
    
  def get_location(self,t):
    ploc=geom3.Vector3(self.planet.get_location(t))
    mloc=geom3.Vector3(self. orbit.get_location(t))
    #print (str(geom3.Point3(mloc+ploc)))
    #print (mloc)
    return (geom3.Point3(mloc+ploc))
  

class SunPlanet(SpaceObject):
  def __init__(self,dataray):
    super(SunPlanet, self).__init__(dataray[0])
    self.orbit=SimpleOrbit(dataray[1],dataray[2],dataray[3],dataray[4],dataray[5],dataray[6],dataray[8])
    self.self_period=dataray[7]
    self.sats=[]

  def get_location(self,t):
    return (self.orbit.get_location(t))

  def  attach_satellite(self,sat):
    sat.attach_to(self)
    self.sats.append(sat)

  def __str__(self):
    s=str(self.name)+'\n'
    for sat in self.sats:
      s+= "    "+str(sat)
      s+='\n'
    return s


class SolarSystem:
  def __init__(self):
    self.sun=Sun()
    self.planets=[]
    for item in planetsArray:
      self.planets.append(SunPlanet(item))
    
    moon=Satellite(Earth_Moons)
    self.planets[2].attach_satellite(moon)
  
  def __str__(self):
    s=""
    s+=str(self.sun)+'\n'
    for p in self.planets:
      s+=str(p)
    s+='\n'
    return s
    

# For tests
def main():
  ss=SolarSystem()
  print (ss)
  
  

# --------------------------------------------------------------------------
if __name__ == '__main__':
        main()


