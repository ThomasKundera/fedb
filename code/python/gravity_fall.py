#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

pi=math.pi
m=1.
s=1.              #second
kg=1.
j=1.              # Joule
W=1*j/s           # Watt

km=1000.*m
mn=60.*s

kGearth=9.81*m/s/s
kGmoon =1.62*m/s/s


def main():
  g=kGmoon
  step=0.01*s
  t0=0
  x0=0
  v0=0
  t=t0
  x=x0
  v=v0
  
  for i in range(int(2./step)):
    print("%d %f %f %f" %(i,t,x,v))
    t+=step
    v=v0+g*(t-t0)
    x=.5*g*t*t # FIXME
    
  
# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()
