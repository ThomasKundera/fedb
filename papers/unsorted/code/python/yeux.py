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

# L'enfant est un parent comme un autre...
class enfant(parent):
  def __init__(self,p1,p2):
    self.herc1=self.mix(p1.herc1,p2.herc1)
    self.herc2=self.mix(p1.herc2,p2.herc2)
    self.gey1 =self.mix(p1.gey1 ,p2.gey1 )
    self.gey2 =self.mix(p1.gey2 ,p2.gey2 )
    self.setEyeColor()
    
  def mix(self,a1,a2):
    if (random.getrandbits(1)):
      return a1
    return a2


def main():
  p1=parent()
  p2=parent()
  print p1
  print p2
  e1=enfant(p1,p2)
  e2=enfant(p1,p2)
  print e1
  print e2
  
    
# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()
