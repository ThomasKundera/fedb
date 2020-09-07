#!/usr/bin/env python

import math

m=1.
km=1000*m
Earth_Radius       = 6371*km

r=Earth_Radius/100
h=1*m

dh=math.sqrt(h*h+2*r*h)

a=math.acos(112*m/r);

print(112*m)
print(r)
print(112*m/r)

print("distance to horizon: "+str(dh)+" m")
print("Angle: "+str(a*180/3.1415))
