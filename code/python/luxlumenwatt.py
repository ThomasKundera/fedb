#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

pi=math.pi
sr=1 # steradian
m=1.
cm=m/100.
km=1000.*m
mile=1.60934*km
W=1.
d=60.*cm
cd=(1./683.)*W/sr # Candela
lm=cd*sr          # Lumen
lx=lm/(m**2)      # Lux

def sph(r):
  return (4./3.)*pi*r**3


CandelMaxDistance=2.6*km
HumanEyeSensitivity=1*cd*4*pi/sph(CandelMaxDistance)

MeasuredFlux=20.*W/(m*m)
SourcePower=MeasuredFlux*sph(d)

print("Source power: "+str(SourcePower)+" W")

print("Human eye sensitivity: "+str(HumanEyeSensitivity)+" W/m²")

SourceFlux=SourcePower/sph(125*mile)
print("Source flux at 125 miles: "+str(SourceFlux)+" W/m²")

print("Source flux ratio human sensitivity: "+str(100*SourceFlux/HumanEyeSensitivity)+"%")
