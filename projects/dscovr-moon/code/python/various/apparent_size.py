#!/usr/bin/env python3
import sys
sys.path.insert(0, "../../../../../code/python/common/")
import math
import solar_system
from solar_system import km

def apparent_angular_size(name,radius,dist):
  alpha=(180/math.pi)*2*math.atan2(radius,dist)
  
  print("Apparent angle of view of "
    +name+" that has a radius of "
    +str(radius/km)+" km from a distance "+str(dist/km)+" km is "
    +str(alpha*60)+"'") # - "+str(alpha))

def main():
  apparent_angular_size("Earth",solar_system.earthRadius,1500000*km)
  apparent_angular_size("Moon",solar_system.moonRadius  ,410000*km)
  apparent_angular_size("Moon",solar_system.moonRadius  ,1500000*km-solar_system.Earth_Moons[1])
  
  
  
# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()



