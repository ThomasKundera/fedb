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

def eyeColorString(color):
    if (color==kBrun):
      return "Brun"
    if (color==kVert):
      return "Vert"
    return "Bleu"
  

class parent:
  def __init__(self):
    self.aleag()
    self.setEyeColor()
    self.eyeColorString=eyeColorString(self.eyeColor)

  def aleag(self):
    self.herc1=random.getrandbits(1)
    self.herc2=random.getrandbits(1)
    
    self.gey1=random.getrandbits(1)
    self.gey2=random.getrandbits(1)
    

  def setEyeColor(self):
    if (self.herc1 or self.herc2):
      self.eyeColor=kBrun
      return
    if (self.gey1 or self.gey2):
      self.eyeColor=kVert
      return
    self.eyeColor=kBleu
    
    
    
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

def simpletest():
  p1=parent()
  p2=parent()
  print p1
  print p2
  e1=enfant(p1,p2)
  e2=enfant(p1,p2)
  print e1
  print e2

class generations:
  def __init__(self,k,color1=None,color2=None):
    self.k=k
    self.c1=color1
    self.c2=color2
    # instanciation de k parents:
    self.parents=[]
    if (color1 != None):
      if (color2==None):
	while(len(self.parents) != self.k):
	  p=parent()
	  if (p.eyeColor == color1):
	    self.parents.append(p)
      else:
	color=[color1,color2]
	colori=0
	while(len(self.parents) != self.k):
	  p=parent()
	  if (p.eyeColor == color[colori]):
	    self.parents.append(p)
	    colori=1-colori
      return
      
    for i in range(self.k):
      self.parents.append(parent())

  def reproduction(self):
    enfants=[]
    for i in range(self.k/2):
      # Les parents font deux enfants
      enfants.append(enfant(self.parents[2*i],self.parents[2*i+1]))
      enfants.append(enfant(self.parents[2*i],self.parents[2*i+1]))
    # Les enfants enterrent leurs parents, et:
    self.parents=enfants
    # Et on shuffle
    random.shuffle(self.parents)
    
  def parentStats(self):
    self.Bvb=[0,0,0]
    for p in self.parents :
      self.Bvb[p.eyeColor]+=1
    self.Bvbpc=[100*self.Bvb[0]/self.k,100*self.Bvb[1]/self.k,100*self.Bvb[2]/self.k]
  
  def __str__(self):
    #for p in self.parents :
    #  print p
    self.parentStats()
    return str(self.Bvb)
  

def doForGeneration(g):
  s=eyeColorString(g.c1)+" "+eyeColorString(g.c2)
  g.reproduction()
  g.parentStats()
  s+=" "+str(g.Bvbpc)
  
  print s


def main():
  doForGeneration(generations(10000,kBrun,kBrun))  
  doForGeneration(generations(10000,kVert,kBrun))  
  doForGeneration(generations(10000,kBleu,kBrun))  
  doForGeneration(generations(10000,kVert,kVert))  
  doForGeneration(generations(10000,kVert,kBleu))
  doForGeneration(generations(10000,kBleu,kBleu))
  
 
 #  for i in range(10):
#    g.reproduction()
#    print g
  

# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()
