#!/usr/bin/env python3
import sys
sys.path.insert(0, './common')

import geom3
import sphere
import solar_system

# http://vmlaker.github.io/pythonwildmagic/ ?

def main():
  ss=solar_system.SolarSystem()
  for t in range(-10800,10800,1000):
    print ("---------------------------------")
    sl=ss.sun.get_location(t)
    el=ss.planets[2].get_location(t)
    ml=ss.planets[2].sats[0].get_location(t)
    
    smvect=sl-ml
    smray=geom3.Ray3(sl,smvect)
    
    earth=sphere.Sphere(el,solar_system.earthRadius)
    
    hits=earth.intersect(smray)
    
    print (hits)
    

# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()


