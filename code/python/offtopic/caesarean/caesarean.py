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
        self.genome=BitArray(random.getrandbits(128))
      case GenomeMethod.kCopy:
        self.genome=genome

  def GetProba(self):
    return (self.genome.count(1)/100.)


class Generation:
  """
  Hold a full generation of a population
  """
  def __init__(self,size=1000,method=GenomeMethod.kParadise):
    self.size=size
    self.pop=[ Individual(method) for i in range(self.size) ]

#  def



def main():
  g=Generation()
  

# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()

