#!/bin/env python

km=1.

Earth_Radius=6371.*km

pi=3.141592653979328


def sphere_volume(r):
  return 4.*pi*r*r*r/3.

def main():
  alt1=300*km
  alt2=600*km
  
  v=sphere_volume(10*km)
  
  v1=sphere_volume(Earth_Radius+alt1)
  v2=sphere_volume(Earth_Radius+alt2)
  
  V=v2-v1
  
  ratio=v/V
  
  snb=2000 # Number of sats
  
  print ("Probability: "+str(snb*100.*ratio)+"%")
  

# --------------------------------------------------------------------------
if __name__ == '__main__':
        main()
