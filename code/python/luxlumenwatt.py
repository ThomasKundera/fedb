#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

pi=math.pi
sr=1 # steradian
m=1.
s=1. #second
j=1. # Joule

W=1*j/s           # Watt

cd=(1./683.)*W/sr # Candela
lm=cd*sr          # Lumen
lx=lm/(m**2)      # Lux

cm=m/100.
mm=m/1000.
km=1000.*m
mile=1.60934*km

eV=1.602e-19*j    # Electron-volt

phE=2*eV # Visible photon: about 2eV

# Human eye
corneaRadius=7.8*mm


def S_sphere(r):
  return (4./3.)*pi*r**3

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


"""
https://fr.wikipedia.org/wiki/Magnitude_limite_visuelle
L'œil humain permet de détecter un flux de 50 à 150 photons par seconde
de lumière verte [...] correspond à une étoile de magnitude 8,5.
"""
def humain_eye_max_sensitivity():
  # Return max sensitivity of human eye in w/m²
  
 # Assuming a treshold of 150 photon/sec/eye surface:
 photon_flux=150/S_disk(corneaRadius)
 print photon_flux
 



def main():
  print (humain_eye_max_sensitivity())


# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()
