#!/usr/bin/env python3
import io,random
import time
import anytree
from anytree.exporter import DotExporter

random.seed(1)

gId=0  # global ID
gPop=0 # To avoid counting pop

# This code is to observe distance to last common ancestor of a population

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
    self.die(maxpop)
    self.reproduce()
  
  def die(self,maxpop):
    global gPop
    if (self.dead): return
    if (random.random()<self.deathcurve[self.age]*(1+gPop/maxpop)):
      self.dead=True
      self.name='*'+self.name
      gPop-=1

  def reproduce(self):
    if (self.dead): return
    if (self.age<=1): return # Also cut recursivity
    for i in range(self.mult):
      c=IdvNode(parent=self)
  
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
    self.year  =  0
    self.maxpop=100  # Max number of individuals in the pop
    self.nby   =200  # run for that many years
    self.start = time.time()

  def doit(self):
    global gPop
    self.f=io.open("datafile.dat","wt")
    self.idvtree=IdvNode()
    
    self.dotGraph()
    
    for i in range(1,self.nby):
      if (not (i % (self.nby/10))):
        delta=int(max(1,time.time()-self.start))
        left=(delta/i)*(self.nby-i)
        print ("Year: "+str(i)+" total pop: "+str(gPop)+" time elaps: "+str(delta)+" time left: "+str(left))
      self.doyear()
      #self.tofile()
    #print(anytree.RenderTree(self.idvtree))
    #DotExporter(self.idvtree).to_picture("idvtree.png")
    self.f.close()

  def doyear(self):
    self.year=self.year+1
    for n in anytree.iterators.preorderiter.PreOrderIter(self.idvtree):
      n.onemoreyear(self.maxpop)
      n.matters=False # reset interest.

    for n in self.idvtree.leaves:
      if (not n.dead):
        n.matters=True
        for n2 in n.ancestors:
          n2.matters=True # FIXME: lots of redundencies here
          
    for n in anytree.iterators.preorderiter.PreOrderIter(self.idvtree):
      if (not n.matters):
        n.parent=None
        #n.name='@'+n.name # debug
        #if (not n.parent.matters):
        #  n.parent=None
    
    lucas=(anytree.util.commonancestors(*self.idvtree.leaves))
    if (len(lucas)):
      self.idvtree=lucas[-1]
    
    self.dotGraph()
    #DotExporter(self.idvtree).to_picture("out/idvtree%5d.png" % self.year)  
    
  def lca(self):
    return #anytree.util.commonancestors(
  
  
  def dotGraph(self):
    DotExporter(self.idvtree).to_dotfile(f'out/idvtree_{self.year:05}.dot')
    
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


