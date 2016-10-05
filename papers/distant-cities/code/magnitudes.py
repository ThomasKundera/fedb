#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

pi=3.14159265358979328


s=1
Hz=1./s

m=1
km=1000*m
Mm=1000*km
Gm=1000*Mm

cm=m/100.
mm=m/1000.
mum=mm/1000.
nm=mum/1000.

UA=150*Gm

Pc=3.09397209368e+13*km

c=297000*km/s

VegaRef=2.52e-23 # W/m²/Hz

SunFlux=3.125e-12 # W/m²/Hz


Rouge=7.4e+14*Hz
Bleu =4.2e+14*Hz

def relatmagParsec(L,d):
  return -2.5*math.log10(L/((d/10)*(d/10)))

def relatmagkm(L,d):
  return relatmagParsec(L,d/Pc)


def DegToRad(d):
  return d*pi/180.

def MinToRad(d):
  return DegToRad(d/60.)

def SecToRad(d):
  return DegToRad(d/3600.)

def Parsec():
  Pc=UA/math.tan(SecToRad(1))
  #print Pc/(300000*3600*24*365.24)
  print Pc

def LightFlux(L,d):
  pass

def LToHz(l):
  return c/l

# --------------------------------------------------------------------------
# Welcome to Derry, Maine
# --------------------------------------------------------------------------
def main():
  #Parsec()
  #print LToHz(700*nm)
  #print 1000/(Rouge-Bleu) # Sun flux
  print math.log(SunFlux/VegaRef)


# --------------------------------------------------------------------------
# Start the command by calling main.
# --------------------------------------------------------------------------
main()
# --------------------------------------------------------------------------

