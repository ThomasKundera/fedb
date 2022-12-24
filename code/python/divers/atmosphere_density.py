#!/usr/bin/env python3

#
# Computing atmospheric density according to:
# https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2018JA026136
#

import sys
sys.path.insert(0, '../common')

import math
from tkunits import kPa, K, Na, R, cm, m, km, earth_radius

# By fitting of the curve on Figure 10 by a 1/r³ function
# we get that constant:
k=30.**3*earth_radius**3

def fdensity(r):
  return(k/r**3)

# The value is in molecule per m⁻³
# So the conversion factor from cm⁻³
def Fdensity(r):
  return (-k/(2*r**2))/(cm**3)


def test_fit():
  for dr in [3,10,20,30,40,50,100]:
    d=dr*earth_radius
    print("f( "+str(d)+" ) = "+str(fdensity(d)))


def main():
  Nb=Fdensity(100*earth_radius)-Fdensity(3*earth_radius)
  
  # PV=nRT
  P=100*kPa
  V=1*m**3
  T=300*K
  n=Na*(P*V/(R*T))
  
  print(Nb/n)
  
  
# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()



