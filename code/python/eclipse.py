#!/usr/bin/env python3
import sys
sys.path.insert(0, './common')

import math
import geom3
import sphere
import solar_system

# http://vmlaker.github.io/pythonwildmagic/ ?

# Real 2017 ones last 193mn, so 11580s

def main():
  ss=solar_system.SolarSystem()
  ppe=None
  step=100
  for t in range(-6900,6900,step):
    print ("---------------------------------")
    sl=ss.sun.get_location(t)
    el=ss.planets[2].get_location(t)
    ml=ss.planets[2].sats[0].get_location(t)
    
    #print (str(t)+" "+str(el)+" "+str(ml))
    
    smvect=ml-sl
    smray=geom3.Ray3(sl,smvect)
    
    earth=sphere.Sphere(el,solar_system.earthRadius)
    
    hit=earth.intersect(smray)
    if (hit):
      #print (str(hit.entry)+" "+str(hit.exit))
      p=smray.start+hit.entry*smray.dir
      if (ppe):
        pe=p-el
        # Earth rotation (FIXME: 2D rotation):
        theta=step*2*math.pi/(3600*24) # crude
        #print (ppe)
        ppe=geom3.Vector3(ppe.dx*math.cos(theta)-ppe.dy*math.sin(theta),ppe.dx*math.sin(theta)+ppe.dy*math.cos(theta),0)
        #print (str(ppe)+" " +str(pe))
        v=1000.*geom3.length(pe-ppe)/step
        vkmh=v*3.6
        print (str(t)+" - "+str(p)+" "+str(v)+" "+str(vkmh))
      ppe=p-el

# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()


