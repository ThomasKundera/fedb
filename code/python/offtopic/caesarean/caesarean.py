#!/usr/bin/env python3

# Toy model about evolution of caesarean section needs in a population

import random
from bitstring import BitArray

#hash = random.getrandbits(128)
#print(hex(hash))
#import binascii
#import codecs

# Perfect genome
kParadiseGenome=BitArray("0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")
class GenomeMethod:
  kParadise=0
  kRandom=1
  kCopy=2


class Individual:
  def __init__(self,method=GenomeMethod.kParadise,genome=kParadiseGenome):
    """
    It can be initialized 3 ways:
    - Paradise (max score genome)
    - Random genome
    - By copying an existing genome
    """
    match method:
      case GenomeMethod.kParadise:
        self.genome=kParadiseGenome
      case GenomeMethod.kRandom:
        self.genome=BitArray(random.getrandbits(128).to_bytes(16,'big'))
      case GenomeMethod.kCopy:
        self.genome=genome

  def GetProba(self):
    return (self.genome.count(1)/100.)

  def mate(self,other):
    ng=BitArray()
    for i in range(len(self.genome)):
      #print([self.genome[i],other.genome[i]])
      c=random.choice([self.genome[i],other.genome[i]])
      if c:
        ng.append(BitArray(bin='0b1'))
      else:
        ng.append(BitArray(bin='0b0'))
    #  print(ng)
    # FIXME: add random mutations
    return Individual(GenomeMethod.kCopy,ng)



class Generation:
  """
  Hold a full generation of a population
  """
  def __init__(self,size=1000,method=GenomeMethod.kParadise):
    self.size=size
    self.pop=[ Individual(method) for i in range(self.size) ]

  def GetPopAverageProba(self):
    s=0
    for ind in self.pop:
      s+=ind.GetProba()
    return (s/self.size)


  def ReproduceOne(self):
    ng=[]
    # Choose parents
    # FIXME: here we can choose two times same parent
    # None will die
    p1=random.choice(self.pop)
    p2=random.choice(self.pop)
    while True:
      child=p1.mate(p2)
      if (random.random() < child.GetProba()):
        # Child alive
        break
      #else:
        #print ("failed: "+str(child.GetProba()))
    return child

  def Reproduce(self):
    ng=[]
    for i in range(self.size):
      ng.append(self.ReproduceOne())
    self.pop=ng


def main():
  g=Generation(1000,GenomeMethod.kRandom)
  for i in range(100):
    print (100*g.GetPopAverageProba())
    g.Reproduce()
  

# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()

