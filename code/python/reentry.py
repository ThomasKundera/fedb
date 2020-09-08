#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

pi=math.pi
m=1.
s=1. #second
kg=1.

j=1. # Joule
W=1*j/s           # Watt

km=1000.*m
mn=60.*s

def main():
  # Reentry of a Soyuz
  M=3000*kg
  d=2.2*m
  Cx=1.
  rho=0.015*kg/(m*m*m)
  v0=7.8*km/s
  
  S=pi*(d/2)*(d/2)
  
  k=.5*rho*S*Cx
  print (k)
  
  v=v0
  t=0
  x=0
  for i in range(8*60):
    F=-k*v*v
    a=F/M
    if (not (i%1)):
      print("At t="+str(t)+" F="+str(round(F))+"N a="+str(round(a))+"ms⁻² v="+str(round(v))+"ms⁻¹ x="+str(round(x))+"m")
    v=v+a
    x=x+v
    t+=1

  

# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()
