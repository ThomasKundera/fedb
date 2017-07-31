#!/usr/bin/env python3
import sys
sys.path.insert(0, './common')
import solar_system



def main():
  ss=solar_system.SolarSystem()
  print (ss.sun.get_location(0))
  print (ss.planets[2].get_location(0))
  print (ss.planets[2].sats[0].get_location(0))
  

# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()


