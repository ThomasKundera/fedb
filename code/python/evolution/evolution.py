#!/usr/bin/env python3
import io,random
import time
import anytree

random.seed(1)

gId=0  # global ID
gPop=0 # To avoid counting pop

# This code is to observe distance to last common ancestor of a population

# --------------------------------------------------------------------------
class Idv(object):
  """Individuals of the population"""
  def __init__(self):
    print ("Idv: __init__(self)")
    global gId
    global gPop
    self.id=gId # Unique ID
    gId+=1
    gPop+=1
    self.age=0
    self.sex=random.getrandbits(1) # not used yet
    self.deathcurve=[.5,.2,.3,.4,.5,.6,.8,1] # Likelihood of dying for each age
    self.mult=5 # How many children
    self.dead=False
  
  def onemoreyear(self,maxpop):
    self.die(maxpop)
    self.reproduce()
  
  def die(self,maxpop):
    global gPop
    print (self.id)
    if (self.dead): return
    if (random.random()<self.deathcurve[self.age]*(1+gPop/maxpop)):
      self.dead=True
      gPop-=1

  def reproduce(self):
    if self.dead: return
    for i in range(self.mult):
      c=IdvNode(parent=self)
  
  def __str__(self):
    return (str(self.id))

class IdvNode(Idv, anytree.NodeMixin):  # Add Node feature
  """Individuals of the population"""
  def __init__(self, parent=None, children=None):
    super(IdvNode, self).__init__()
    self.parent = parent
    if children:  # set children only if given
      self.children = children

  def __str__(self):
    return super(IdvNode, self).str()

# --------------------------------------------------------------------------
class Pop(object):
  def __init__(self):
    self.year  =  0
    self.maxpop=100. # Max number of individuals in the pop
    self.nby   =  2  # run for that many years
    self.start = time.time()

  def doit(self):
    self.f=io.open("datafile.dat","wt")
    self.idvtree=IdvNode()
    
    #n=anytree.Node('toto')
    #for t in n.PreOrderIter():
    #  print(t)
    
    for i in range(1,self.nby):
      if (not (i % (self.nby/10))):
        delta=int(max(1,time.time()-self.start))
        left=(delta/i)*(self.nby-i)
        print ("Year: "+str(i)+" time elaps: "+str(delta)+" time left: "+str(left))
        print(anytree.RenderTree(self.idvtree))
      self.doyear()
      #self.tofile()
    self.f.close()

  def doyear(self):
    self.year=self.year+1
    for n in anytree.iterators.preorderiter.PreOrderIter(self.idvtree):
      n.onemoreyear(self.maxpop)
    print(anytree.RenderTree(self.idvtree))
    
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



# --------------------------------------------------------------------------
def main():
  p=Pop()
  p.doit()


# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()


