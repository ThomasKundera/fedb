#!/usr/bin/env python3

#
# Computing atmospheric density according to:
# https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2018JA026136
#

import sys
sys.path.insert(0, '../common')

import math
from tkunits import cm, km, earth_radius

# By fitting of the curve on Figure 10 by a 1/r³ function
# we get that constant:
k=30.**3*earth_radius**3

def fdensity(r):
    return(k/r**3)


def main():
  for dr in [3,10,20,30,40,50,100]:
    d=dr*earth_radius
    print("f( "+str(d)+" ) = "+str(fdensity(d)))

    F=-3
  
# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()



