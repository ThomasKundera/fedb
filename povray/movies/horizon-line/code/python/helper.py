#!/usr/bin/env python

import math

m=1
km=1000*m
Earth_Radius       = 6371*km

r=Earth_Radius/1000
h=1*m

dh=math.sqrt(h*h+2*r*h)


print("distance to horizon: "+str(dh)+" m")
