#!/usr/bin/env python
import sys
import os
import re
import matplotlib.pyplot as plt
import networkx as nx

DATADIR="data"

class NameSurname:
  def __init__(self,s):
    self.name=""
    self.surnames=[]
    bits=s.split()
    for b in bits:
      if (b.isupper()):
        self.name+=b
      else:
        self.surnames.append(b)

  def __str__(self):
    s=self.name
    for sn in self.surnames:
      s+=" "+sn
    return s

def CollectData(n):
  files=os.listdir(DATADIR)
  for fn in files:
    if (re.match("res-.*.html.txt",fn)):
      f=open(os.path.join(DATADIR,fn),"rt")
      for line in f.readlines():
        if (not line.isspace()):
          n.append(NameSurname(line))
 
 

def FillDicts(names,namedict,surnamedict):
  for n in names:
    if (not (n.name in namedict)):
      d={}
      for ns in n.surnames:
        d[ns]=1
      namedict[n.name]=d
    else:
      for ns in n.surnames:
        if ns in namedict[n.name]:
          namedict[n.name][ns]=namedict[n.name][ns]+1
        else:
          namedict[n.name][ns]=1
    for ns in n.surnames:
      if (not (ns in surnamedict)):
        d={}
        d[n.name]=1
        surnamedict[ns]=d
      else:
        if (n.name in surnamedict[ns]):
          surnamedict[ns][n.name]=surnamedict[ns][n.name]+1
        else:
          surnamedict[ns][n.name]=1


def main():
  names=[]
  CollectData(names)
  print("Number of items: "+str(len(names)))
  namedict={}
  surnamedict={}
  
  FillDicts(names,namedict,surnamedict)
          
  G = nx.Graph()
  ntest=0
  
  for sn in surnamedict:
    ntest+=1
    if (ntest>10): break
    print("\n"+sn)
    if (not G.has_node(sn)): G.add_node(sn)
    for n in surnamedict[sn]:
      print(n)
      for nsn in namedict[n]:
        print(nsn)
        if ((nsn != sn)): # same surname avoided
          if (not G.has_node(nsn)): G.add_node(nsn)
          if (not G.has_edge(sn,nsn)):
            G.add_edge(sn,nsn,weight=namedict[n][sn]+namedict[n][nsn]+0.0)
            #G.add_edge(sn,nsn,weight=1)
          else:
            #print("hop: "+sn+" "+nsn)
            #print(G[sn][nsn])
            G.add_edge(sn,nsn,weight=namedict[n][sn]+G[sn][nsn]["weight"])
          #print(eatn[n][sn])
 
  nx.draw(G)
  plt.draw()
  
# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()


