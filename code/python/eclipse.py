#!/usr/bin/env python3
import sys
sys.path.insert(0, './common')
import solar_system



def main():
  ss=solar_system.SolarSystem()
  for t in range(-3600,3600,1000):
    print (ss.sun.get_location(t))
    print (ss.planets[2].get_location(t))
    print (ss.planets[2].sats[0].get_location(t))
  

# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()


