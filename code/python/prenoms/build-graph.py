#!/usr/bin/env python3
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
 
 

def FillDictsFilter(names,namedict,surnamedict):
  itest=0
  ntest=200
  nd={}
  sd={}
  for n in names:
    itest+=1
    if (itest>ntest): break
    if (not (n.name in nd)):
      d={}
      for ns in n.surnames:
        d[ns]=1
      nd[n.name]=d
    else:
      for ns in n.surnames:
        if ns in nd[n.name]:
          nd[n.name][ns]=nd[n.name][ns]+1
        else:
          nd[n.name][ns]=1
    for ns in n.surnames:
      if (not (ns in sd)):
        d={}
        d[n.name]=1
        sd[ns]=d
      else:
        if (n.name in sd[ns]):
          sd[ns][n.name]=sd[ns][n.name]+1
        else:
          sd[ns][n.name]=1
  surnamedict=sd #dict(sd)
  namedict=nd # dict(nd)
  return
  # Cleaning up seldom used surnames
  for ns in sd:
    l=0
    for n in sd[ns]:
      l+=sd[ns][n]
    #print(l)
    if (l>=0):
      print(ns)
      surnamedict[ns]=dict(sd[ns])
  
  for n in nd:
    l=0
    for ns in n:
      d={}
      if (ns in surnamedict):
        l+=nd[n][ns]
        d[ns]=nd[n][ns]
    namedict[n]=d
  print(len(nd))
  print(len(sd))
  print(len(namedict))
  print(len(surnamedict))
  

def FillDicts(names):
  namedict={}
  surnamedict={}

  itest=0
  ntest=200
  
  for n in names:
    itest+=1
    if (itest>ntest): break
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

  return (namedict,surnamedict)


def main():
  names=[]
  CollectData(names)
  print("Number of items: "+str(len(names)))
  
  (namedict,surnamedict)=FillDicts(names)
  #return
  
  G = nx.Graph()
  ntest=0
  tmax=40
  
  #print(namedict["GAUDENZI"])
  
  #surnamedict["Manon"]=[] # Too many for tests
  
  for sn in surnamedict:
    ntest+=1
    if (ntest>tmax): break
    print("\n--\n"+sn)
    if (not G.has_node(sn)): G.add_node(sn)
    for n in surnamedict[sn]:
      if (ntest>tmax): break
      print('\n'+n)
      for nsn in namedict[n]:
        ntest+=1
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
          #print(eatn[n][sn]) with_labels = True)
  # Reverse weights
  for u,v,d in G.edges(data=True):
    d['weight']=1./d['weight']
  
  print("===== LOADED ======")
  print("Graph size: "+str(len(G)))
  nx.draw(G, with_labels = True)
  plt.show()
  
# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()


