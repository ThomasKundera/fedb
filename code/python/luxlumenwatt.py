#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

pi=math.pi
sr=1 # steradian
m=1.
s=1. #second
j=1. # Joule

W=1*j/s           # Watt

cd=(1./683.)*W/sr # Candela: in practice divide by 6 for human eye efficiency
eye_eff=100./683. # About the energy efficiency ratio for Sun to human eye
lm=cd*sr          # Lumen
lx=lm/(m**2)      # Lux

cm=m/100.
mm=m/1000.
km=1000.*m
ligh_year=9.4607e15*m 


eV=1.602e-19*j    # Electron-volt
Eph=2*eV # Visible photon energy: about 2eV

# Midde-age units
mile=1.60934*km


# Human eye
corneaRadius=7.8*mm


def V_sphere(r):
  return (4./3.)*pi*r**3

def S_sphere(r):
  return 4.*pi*r*r

def S_disk(r):
  return 2.*pi*r*r

def old():
  d=60.*cm
  CandelMaxDistance=2.6*km
  HumanEyeSensitivity=1*cd*4*pi/sph(CandelMaxDistance)

  MeasuredFlux=20.*W/(m*m)
  SourcePower=MeasuredFlux*sph(d)

  print("Source power: "+str(SourcePower)+" W")

  print("Human eye sensitivity: "+str(HumanEyeSensitivity)+" W/m²")

  SourceFlux=SourcePower/sph(125*mile)
  print("Source flux at 125 miles: "+str(SourceFlux)+" W/m²")

  print("Source flux ratio human sensitivity: "+str(100*SourceFlux/HumanEyeSensitivity)+"%")


def magnitude_factor(m1,m2):
  # m1=-2.5log10(f1/f0) m2=-2.5log10(f2/f0)
  # => f2/f1 = 10^(.4*(m2-m1))
  return (math.pow(10,.4*(m2-m1)))
  
"""
https://fr.wikipedia.org/wiki/Magnitude_limite_visuelle
L'œil humain permet de détecter un flux de 50 à 150 photons par seconde
de lumière verte [...] correspond à une étoile de magnitude 8,5.
"""
def human_eye_max_sensitivity():
  # Return max sensitivity of human eye in w/m²
  
  # Assuming a treshold of 150 photon/sec/eye surface:
  min_illumin=150*Eph/S_disk(corneaRadius) # illuminance in lux

  # However, we know that the best magnitute that can reasonably be seen is 6, not 8.5
  # So we'll fix it with a conservative approach
  # (a 2.5 diff in magnitute means a factor 10, btw)
  return magnitude_factor(6,8.5)*min_illumin
  

def apparent_magnitude_to_irradiance(m):
  return (human_eye_max_sensitivity()*magnitude_factor(m,6.))

def irradiance_to_isotropic_power(ir,d):
  return (ir*S_sphere(d))

def oldmain():
  # Computing the power of a source at 125 miles that would be
  # a magnitude 6 visibility (realistic treshold)
  P=human_eye_max_sensitivity()*S_sphere(125*mile)
  print("P (125 miles)= "+str(P)+"W")
  P=human_eye_max_sensitivity()*S_sphere(3*ligh_year)
  print("P (3 light years)= "+str(P)+"W")
  P=human_eye_max_sensitivity()*S_sphere(125*mile)
  print("P = "+str(P)+"W")

def main():
  # Computing absolute light power of a satellite at 300 "miles"
  # that has an apparent magnitude of 4:
  m=3
  d=300*mile
  ir=apparent_magnitude_to_irradiance(m)/eye_eff
  P=irradiance_to_isotropic_power(ir,d)
  print ("Total isotropic power of a source at 300 miles that has a magnitude of 4: "+str(P)+" W")

# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()
