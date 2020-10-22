#!/usr/bin/env python
import sys
sys.path.insert(1, 'common')
from tkunits import *

h=400*km
r=earth_radius
M=earth_mass
G=gravitational_constant

g0=G*M/((r+h)*(r+h))
f0=-g0

print(g0)

gh=G*M/(r*r)
fh=f0*r/(r+h)

dg=(gh-g0)/h
df=(fh-f0)/h

print(dg)
print(df)

x=400*km

# Paracorde 550: 7.4g/m
# Source: Facebook
ml=7.4*g/m

P=ml*((g0+f0)*x+.5*(dg+df)*x*x)

print (P)
