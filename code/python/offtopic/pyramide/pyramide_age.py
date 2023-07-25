#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def read_file():
  f=open("pyramide_age.csv","rt")
  al=[]
  fl=[]
  ml=[]
  for line in f:
    items=line.strip().split(';')
    age=float(items[0])
    fem=float(items[1])
    mal=float(items[2])
    al.append(age)
    fl.append(fem)
    ml.append(mal)
  f.close()
  return (al,fl,ml)


def main():
  (al,fl,ml)=read_file()
  
  nal=[]
  rl=[]
  zl=[]
  for a,f,m in zip(al,fl,ml):
    if (a>100): break
    nal.append(a)
    if (f>0):
      rl.append(100*(m/f-1.))
    else:
      rl.append(0)
    zl.append(0)
  
  plt.plot(nal, rl, color='purple')
  plt.plot(nal, zl, color='steelblue', linestyle='--', linewidth=2)
  plt.show()

  

# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()

