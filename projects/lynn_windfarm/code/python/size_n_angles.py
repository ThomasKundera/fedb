#!/usr/bin/env python3
import math

from tkunits import km, m, mm, μm

# Captor size
lx = 35.9*mm
ly = 24.0*mm

# Captor pixel size
px = 6240.
py = 4160.

# Captor pixel pitch
dx = lx/px
dy = ly/py

# Assumed square pixel
dxy = (dx+dy)/2.

# Focale
f = 600.0*mm

def pxtoangle(pxl):
    return 2.*math.atan2(pxl*dxy,2*f)

def angletodistance(a,l):
    # Object has a real size l (in meter)
    # And is viewed under an angle a
    # Return the distance of the object
    # from the captor
    # l=d*math.tan(a)
    # d = l/tan(a)
    return l/math.tan(a)

def main():
    print("dxy = "+str(dxy/μm)+" μm")
    pxl=py/2
    print("l = "+str(pxl*dxy/mm)+" mm")
    print("a = "+str(180*pxtoangle(pxl)/math.pi)+" deg")
    s=100*m
    print("d = "+str(angletodistance(pxl*dxy,s)/km)+" km")
    

# if main call main
if __name__ == "__main__":
    main()
