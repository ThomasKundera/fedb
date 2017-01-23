#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Units
# Distance
m=1.
km=1000.*m
UA=149597870700*m
# Time
s=1.
Y=31556925.98*s
# Mass
kg=1.

#derivatives
N=kg*m/(s*s)

# Constants

G=6.67E-11*N*m*m/(kg*kg)


# Wikipedia
# Demi-grand axe (UA)	Excentricité	Inclinaison (°)	Période (années) Mass (kg)

planetsArray=[
  ["Mercure" ,  0.38710 , 0.205631 ,  7.0049  ,   0.2408  ,  330.2E21  ],
  ["Vénus"   ,  0.72333 , 0.006773 ,  3.3947  ,   0.6152  , 4.8685E24  ],
  ["Terre"   ,  1.00000 , 0.016710 ,  0.00000 ,   1.00000 , 5.9736E24  ],
  ["Mars"    ,  1.52366 , 0.093412 ,  1.8506  ,   1.8808  , 641.85E21  ],
  ["Cérès"   ,  2.7665  , 0.078375 , 10.5834  ,   4.601   ,   9.46E20  ],
  ["Jupiter" ,  5.20336 , 0.048393 ,  1.3053  ,  11.862   , 1.8986E27  ],
  ["Saturne" ,  9.53707 , 0.054151 ,  2.4845  ,  29.457   , 568.46E24  ],
  ["Uranus"  , 19.1913  , 0.047168 ,  0.7699  ,  84.018   , 8.6810E25  ],
  ["Neptune" , 30.0690  , 0.008586 ,  1.7692  , 164.78    , 102.43E24  ],
  ["Pluton"  , 39.4817  , 0.248808 , 17.1417  , 248.4     ,  1.314E22  ],
  ["Éris"    , 68.1461  , 0.432439 , 43.7408  , 562.55    ,   1.66E22  ]
]

sunMass=1.9891E30*kg


def graviForce(m,M,d):
  return -G*m*M/(d*d)

class Planet:
  def __init__(self,pal):
    self._name  =pal[0]
    self._dist  =pal[1]*UA
    self._period=pal[4]*Y
    self._mass  =pal[5]*kg
  
  def __str__(self):
    return self._name+" "+str(self._dist)+" "+str(self._mass)
  
  
  def SunForce(self):
    print ("For "+self._name+" : "+"{:.2E}".format(graviForce(sunMass,self._mass,self._dist)))

def main():
  plist=[]
  for pal in planetsArray:
    plist.append(Planet(pal))
  
  for p in plist:
    p.SunForce()

# --------------------------------------------------------------------------
if __name__ == '__main__':
        main()
