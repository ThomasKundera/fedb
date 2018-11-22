#!/usr/bin/env python3
import random

random.seed(1)

gMutN=0



class Mutations(object):
  def __init__(self,m):
    global gMutN
    gMutN+=1
    self.m=gMutN
    self.mother=m
  
  def label(self,n):
    try: # do not relabel
      return(self.lbl)
    except AttributeError:
      self.lbl=n
    if (self.mother):
      self.mother.label(n+1)

  def label_check(self,n):
    try:
      return(max(self.lbl,n))
    except AttributeError:
      self.lbl=n
      return(self.mother.label_check(n+1))

  def unlabel(self):
    try:
      del self.lbl
      self.mother.unlabel()
    except AttributeError:
      return
    

  def lca(self,o):
    self.label(0)
    v=o.label_check(0)
    #self.unlabel() #Should be done, but we want to measure lots of lcu
    #o.unlabel()
    return (v)
    

class Idv(object):
  def __init__(self,m):
    self.mut=Mutations(m)
    self.age=0
    self.sex=random.getrandbits(1) # not used yet
    self.deathcurve=[.5,.2,.3,.4,.5,.6,.8,1]
    self.mult=5
   
  def kill(self,surpop):
   return (random.random()<self.deathcurve[self.age]*(1+surpop))

  def reproduce(self,idvl):
    for i in range(self.mult):
      idvl.add(Idv(self.mut))

  def __str__(self):
    return (str(self.age))
  
  def lca(self,o):
    return(self.mut.lca(o.mut))

  def unlabel(self):
    self.mut.unlabel()


class Pop(object):
  def __init__(self):
    self.maxpop=1000.;
    
  def doit(self):
    self.idvl=set()
    self.idvl.add(Idv(None))
    
    for i in range(2000):
      self.year()
      self.Print()

  def year(self):
    newdv=set()
    kdv=set()
    for idv in self.idvl:
      if (idv.kill(len(self.idvl)/self.maxpop)):
        kdv.add(idv)
      else:
        idv.reproduce(newdv)
    for idv in newdv:
      self.idvl.add(idv)
    for idv in kdv:
      self.idvl.remove(idv)
  
  def extract_some(self,n):
    s=[]
    for idv in self.idvl:
      s.append(idv)
      n-=1
      if (n<=0):
        return s
    return s # when not enouth elements
  
  def lca(self,s):
    # testing all agains each other is large.
    # testing just first against others
    n=0
    sm=0
    for i in range(1,len(s)):
      sm=max(sm,s[0].lca(s[i]))
      n+=1
    
    for idv in s:
      idv.unlabel()
    
    print(sm) # just to avoid 0
      
    
  
  def Print(self):
    print("Pop is now: "+str(len(self.idvl)))
    s=self.extract_some(100)
    lca=self.lca(s)
    
    
    
def main():
  p=Pop()
  p.doit()


# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()


