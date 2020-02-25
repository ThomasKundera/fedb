#!/usr/bin/env python3
import io,random
import time
import anytree
from anytree.exporter import DotExporter

random.seed(1)

gId=0   # global ID
gPop=0  # To avoid counting those who are alive
gStep=0 # Graphic steps
gYear=0

# This code is to observe distance to last common ancestor of a population

def dotGraph(n,l=0):
  global gStep
  global gYear
  if (l>1): return
  DotExporter(n).to_dotfile(f'out/idvtree_{gYear:05}_{gStep:05}.dot')
  gStep+=1


# --------------------------------------------------------------------------
class Idv(object):
  """Individuals of the population"""
  def __init__(self):
    global gId
    global gPop
    self.id=gId # Unique ID
    gId+=1
    gPop+=1
    self.age=0
    self.sex=random.getrandbits(1) # not used yet
    self.deathcurve=[.5,.2,.3,.4,.5,.6,.8,1] # Likelihood of dying for each age
    self.mult=3 # How many children
    self.dead=False
    self.matters=False
  
  def onemoreyear(self,maxpop):
    self.age+=1
    a=self.die(maxpop)
    b=self.reproduce()
    return a or b # python will optimize, but both have to be done
  
  def die(self,maxpop):
    global gPop
    if (self.dead): return False
    if (random.random()<self.deathcurve[self.age]*(1+gPop/maxpop)):
      self.dead=True
      self.name='*'+self.name
      gPop-=1
      return True
    return False

  def reproduce(self):
    if (self.dead): return False
    if (self.age<=1): return False # Also cut recursivity
    for i in range(self.mult):
      c=IdvNode(parent=self)
    return True
  
  def __str__(self):
    if (self.dead): return '*'+str(self.id)
    return (str(self.id))

class IdvNode(Idv, anytree.NodeMixin):  # Add Node feature
  """Individuals of the population"""
  def __init__(self, parent=None, children=None):
    super(IdvNode, self).__init__()
    self.name=str(self.id)
    self.parent = parent
    if children:  # set children only if given
      self.children = children

  def __str__(self):
    return super(IdvNode, self).__str__()
  
  def __repr__(self):
    return super(IdvNode, self).__str__()

# --------------------------------------------------------------------------
class Pop(object):
  def __init__(self):
    global gYear
    gYear  =  0
    self.maxpop=200  # Max number of individuals in the pop
    self.nby   =500  # run for that many years
    self.start = time.time()

  def doit(self):
    global gPop
    global gYear
    self.f=io.open("datafile.dat","wt")
    self.idvtree=IdvNode()
    
    dotGraph(self.idvtree)
    
    for i in range(1,self.nby):
      if (not (i % (self.nby/10))):
        delta=int(max(1,time.time()-self.start))
        left=(delta/i)*(self.nby-i)
        print ("Year: "+str(i)+" total pop: "+str(gPop)+" LUCA depth:"+str(self.idvtree.height)+" time elaps: "+str(delta)+" time left: "+str(left))
      self.doyear()
      self.f.write(str(gYear)+" "+str(gPop)+" "+str(self.idvtree.height)+'\n')
    self.f.close()

  def doyear(self):
    global gYear
    global gStep
    gYear+=1
    gStep=0
    alivelist=[]
    for n in anytree.iterators.preorderiter.PreOrderIter(self.idvtree):
      if (n.onemoreyear(self.maxpop)):
        dotGraph(self.idvtree,2) # only draw if there is a change. FIXME: idvtree global?
      n.matters=False # reset interest.
      if (not n.dead): alivelist.append(n)
      
    for n in alivelist:
      #if (not n.dead): this is a give now
      n.matters=True
      for n2 in n.ancestors:
        n2.matters=True # FIXME: lots of redundencies here
          
    for n in anytree.iterators.preorderiter.PreOrderIter(self.idvtree):
      if ((n.dead) and (not n.matters)):
        n.parent=None
        dotGraph(self.idvtree,2)
    
    lucas=(anytree.util.commonancestors(*alivelist))
    if (len(lucas)):
      self.idvtree=lucas[-1] 
      #for n in lucas: # This is only for movies
      #  self.idvtree=n
      #  dotGraph(self.idvtree,2)
    
    dotGraph(self.idvtree)
    
  def lca(self):
    return #anytree.util.commonancestors(
  
  
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


