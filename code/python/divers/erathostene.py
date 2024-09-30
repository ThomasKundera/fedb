#!/usr/bin/env python3
import sys
import math
from math import pi
sys.path.insert(0, '../common')
from tkunits import km

# convert from degrees to radians
def d2r(d):
    return d*(pi/180)

def main():
    # ABC triangle
    # AB=800km
    AB=800*km
    # BAC: 90-7.2°
    bac=d2r(90-7.2)
    # BC=AB*tan(90-7.2°)
    BC=AB*math.tan(bac)
    # Remove decimals for print
    print("BC="+str(BC/km).split(".")[0]+" km")



  
  
  
# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()



