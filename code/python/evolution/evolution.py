#!/usr/bin/env python3
import io,random
import time

random.seed(1)

gMutN=0


class Mutations(object):
  def __init__(self,m):
    global gMutN
    gMutN+=1
    self.m=gMutN
    self.mother=m
  
  def label_rec(self,n):
    try: # do not relabel
      return(max(self.lbl,n))
    except AttributeError:
      self.lbl=n
    if (self.mother):
      self.mother.label(n+1)
    return(n+1)

  def unlabel_rec(self):
    try:
      del self.lbl
      self.mother.unlabel()
    except AttributeError:
      return
  
  def label(self,n):
    # Rewrote as non recursive (recursion depth in python is limited)
    # it's anyway most of the time faster and less memory consuming
    try: # do not relabel
      return(max(self.lbl,n))
    except AttributeError:
      self.lbl=n
    p=self.mother
    while(p):
      n+=1
      try: # do not relabel
        return(max(p.lb,n))
      except AttributeError:
        p.lbl=n
        p=p.mother
    return(n)
    
  def label_check_rec(self,n):
    try:
      return(max(self.lbl,n))
    except AttributeError:
      self.lbl=n
      return(self.mother.label_check(n+1))

  def label_check(self):
    p=self
    n=0
    while (p):
      try:
        return(max(p.lbl,n))
      except AttributeError:
        p=p.mother
        n+=1
    
    print("ERROR: Mutations.label_check(): unreachable statement")
    raise
    
  def unlabel(self):
    p=self
    try:
      while (p):
        del p.lbl
        p=p.mother
    except AttributeError:
      return
    

  def lca(self,o):
    self.label(0)
    v=o.label_check()
    self.unlabel() # has to be done in general
    o.unlabel()
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
    self.y=0
    self.maxpop=10000.
    self.nby=2000
    self.start = time.time()

  def doit(self):
    self.f=io.open("datafile.dat","wt")
    self.idvl=set()
    self.idvl.add(Idv(None))
    
    for i in range(1,self.nby):
      if (not (i % (self.nby/10))):
        delta=int(max(1,time.time()-self.start))
        left=(delta/i)*(self.nby-i)
        print ("Year: "+str(i)+" time elaps: "+str(delta)+" time left: "+str(left))
      self.year()
      self.tofile()
    self.f.close()


  def year(self):
    self.y=self.y+1
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
    return(sm)
    
  def tofile(self):
    s=self.extract_some(100)
    lca=self.lca(s)
    self.f.write(str(self.y)+" "+str(len(self.idvl))+" "+str(lca)+'\n')

def main():
  p=Pop()
  p.doit()


# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()


