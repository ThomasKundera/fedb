#!/usr/bin/env python

import random

kBrun=0
kVert=1
kBleu=2

# Using http://genetics.thetech.org/sites/default/files/EyeColorChart2.gif
# herc2:
# false is b
# true  is B
# gey:
# false is b
# true is G

class parent:
  def __init__(self):
    self.aleag()
    self.setEyeColor()

  def aleag(self):
    self.herc1=random.getrandbits(1)
    self.herc2=random.getrandbits(1)
    
    self.gey1=random.getrandbits(1)
    self.gey2=random.getrandbits(1)
    

  def setEyeColor(self):
    if (self.herc1 or self.herc2):
      self.eyeColor=kBrun
      self.eyeColorString="Brun"
      return
    if (self.gey1 or self.gey2):
      self.eyeColor=kVert
      self.eyeColorString="Vert"
      return
    self.eyeColor=kBleu
    self.eyeColorString="Bleu"
    
    
    
  def __str__(self):
    if (self.herc1): s='B'
    else: s='b'
    if (self.herc2): s+='B'
    else: s+='b'
    s+=" "
    if (self.gey1): s+='G'
    else: s+='b'
    if (self.gey2): s+='G'
    else: s+='b'
    s+=" "+self.eyeColorString
    return s


def main():
  p1=parent()
  p2=parent()
  
  print p1
  print p2
    
# --------------------------------------------------------------------------
if __name__ == '__main__':
        main()
