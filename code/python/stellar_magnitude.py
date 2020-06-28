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
ligh_year=9.4607e15*m
au=149597870700*m
parsec=au*648000/pi # By definition

eV=1.602e-19*j    # Electron-volt
Eph=2*eV # Visible photon energy: about 2eV

# Midde-age units
mile=1.60934*km

# Sun standard bolometric power
L0_sun=3.828e26*W
# Sun standard absolute magnitude
M_sun=4.74
# Sun irradiance at 1 au
Ir_au_sun=1361*W/m**2

def V_sphere(r):
  return (4./3.)*pi*r**3

def S_sphere(r):
  return 4.*pi*r*r

def S_disk(r):
  return 2.*pi*r*r

def magnitude_factor(m1,m2):
  # m1=-2.5log10(f1/f0) m2=-2.5log10(f2/f0)
  # => f2/f1 = 10^(.4*(m2-m1))
  return (math.pow(10,.4*(m2-m1)))
  
def irradiance_to_isotropic_power(ir,d):
  return (ir*S_sphere(d))

def luminosity_to_bolometric_absolute_magnitude(P):
  # https://en.wikipedia.org/wiki/Absolute_magnitude#Bolometric_magnitude
  L0=3.0128e28*W
  return (-2.5*math.log10(P/L0))

def bolometric_absolute_magnitude_to_luminosity(M):
  # https://en.wikipedia.org/wiki/Absolute_magnitude#Bolometric_magnitude
  L0=3.0128e28*W
  return (L0*math.pow(10,-.4*M))

def bolometric_absolute_magnitude_to_irradiance(M,d):
  L=bolometric_absolute_magnitude_to_luminosity(M)
  return (L/S_sphere(d))

def bolometric_relative_magnitude_to_irradiance(m):
  f0=bolometric_absolute_magnitude_to_irradiance(0,10*parsec)
  return (f0*math.pow(10,-0.4*m))
  

def self_coherency():
  print("M_sun  =\t\t4.74\t=\t"
    +str(luminosity_to_bolometric_absolute_magnitude(L0_sun)))
  print("L0_sun =\t3.828×10²⁶W\t=\t"
    +str(bolometric_absolute_magnitude_to_luminosity(M_sun)))
  print("Ir_au_sun =\t1361W/m²\t=\t"+
        str(bolometric_absolute_magnitude_to_irradiance(M_sun,au)))
  print("ϕ0 =\t??W/m²\t=\t"+
        str(bolometric_absolute_magnitude_to_irradiance(0,10*parsec)))
  print("Ir_au_sun =\t??\t=\t"+
        str(bolometric_relative_magnitude_to_irradiance(-26.832)))
  
  
def main():
  # Computing absolute light power of a satellite at 300 "miles"
  # that has an apparent magnitude of 3:
  #self_coherency()
  m=3
  d=300*mile
  f=bolometric_relative_magnitude_to_irradiance(m)
  print("Irradiance of a mag "+str(m)+" object: "+str(f)+" W/m²")
  P=irradiance_to_isotropic_power(f,300*mile)
  print("Isotropic power of a "+str(d)+" m away object: "+str(P)+" W")
  s=P/(0.8*Ir_au_sun)
  print("Equivalent Sun surface of such object with a 80% reflectivity: "+str(s)+" m²")
  
  print (130e6*ligh_year/mile)
  print (130e6*365.4*24)
  
# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()










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

def old2():
  # Computing the power of a source at 125 miles that would be
  # a magnitude 6 visibility (realistic treshold)
  P=human_eye_max_sensitivity()*S_sphere(125*mile)
  print("P (125 miles)= "+str(P)+"W")
  P=human_eye_max_sensitivity()*S_sphere(3*ligh_year)
  print("P (3 light years)= "+str(P)+"W")
  P=human_eye_max_sensitivity()*S_sphere(125*mile)
  print("P = "+str(P)+"W")

def old3():
  # Computing absolute light power of a satellite at 300 "miles"
  # that has an apparent magnitude of 3:
  m=3
  d=300*mile
  ir=apparent_magnitude_to_irradiance(m)/eye_eff
  P=irradiance_to_isotropic_power(ir,d)
  # Suppose a 50% reflexive surface, moreover, surface won't be perfectly normal to both Sun and observator, asuming a 30° angle we add (√3/2)²=3/4 factor:
  P=(3./4.)*2*P
  # Total surface needed:
  S=P/Ir_sun
  print ("Total isotropic power of a source at 300 miles that has a magnitude of 4: "+str(P)+" W, so a surface of "+str(S)+" m²")

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
  # Here, we assume that astronomical 6 is 8.5 threshold.
  return (human_eye_max_sensitivity()*magnitude_factor(m,8.5))

# Human eye
corneaRadius=7.8*mm
eye_eff=100./683. # About the energy efficiency ratio for Sun to human eye
