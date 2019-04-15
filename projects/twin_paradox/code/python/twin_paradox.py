#!/usr/bin/env python3

import sys
import math

c=1
s=1

def gamma(v):
  return 1./(math.sqrt(1-v*v/(c*c)))



class FourVect: # In one space dimentions, we cheat
  def __init__(self,x,t):
    self.x=x
    self.t=t

  def __str__(self):
    return '[ x='+str(self.x)+' , t='+str(self.t)+' ]' 

def lorentz(ev,v):
  xp=gamma(v)*(  ev.x  -ev.t*v      )
  tp=gamma(v)*(  ev.t  -ev.x*v/(c*c))
  return FourVect(xp,tp)
 
def invlorentz(ev,v):
  xp=gamma(v)*(  ev.x  +ev.t*v      )
  tp=gamma(v)*(  ev.t  +ev.x*v/(c*c))
  return FourVect(xp,tp)

class Frame(FourVect):
  def __init__(self,lbl,x0,t0): # In my own frame, v=0
    FourVect.__init__(self,x0,t0)
    self.lbl=lbl
    self.flist=[]
    self.rec=0 # trick for recursive attachements
 
 
  def AttachFrameNonRec(self,f,v): # Attach frame f of speed v in self.
    self.flist.append([f,v])

  def AttachFrame(self,f,v): # Attach frame f of speed v in self.
    self.flist.append([f,v])
    # inverse attachement:
    f.AttachFrameNonRec(self,-v) # Speed are seen as symetric in each referential
  
  def SeingEvent(self,ev):
    print("\nEvent "+str(ev)+" in "+self.lbl+" :") 
    for f in self.flist:
      print("Is in "+f[0].lbl+" seen as "+str(lorentz(ev,f[1]))+" (gamma= "+str(gamma(f[1]))+" )")
    
      
  
  def str_non_rec(self):
    return "Frame "+self.lbl+' : '+FourVect.__str__(self)
  
  def __str__(self):
    s="\nFrame "+self.lbl+' : '+FourVect.__str__(self)
    for f in self.flist:
      s+="\nAttached to "+f[0].str_non_rec()+" seen at speed "+str(f[1])
    return s
         
# --------------------------------------------------------------------------
def main():
  #  0              L              2L
  #  A
  #  B
  #                 |               C

  v=.01*c
  L=c*10*s # 10 light-seconds.
  g=gamma(v)
  
  A=Frame("A",   0, 0  )
  B=Frame("B",   0, 0  )
  C=Frame("C",   0, 0  )
  
  A.AttachFrame(B, v)
  A.AttachFrame(C,-v)
  
  # I : At start 
  print("============== [I]: at start position")
  print(A)
  print(B)
  print(C)
  
  # I From A, B and C crossing at L
  print("=============== [I]: at Start position")
  ev1=FourVect(0,0)
  A.SeingEvent(ev1)
  
  # stuff
  #print("=============== [01]: Stuff")
  #ev01=FourVect(0,1)
  #A.SeingEvent(ev01)
  
  # II From A, B and C crossing at L
  print("=============== [II]: B and C crossing at L")
  ev2=FourVect(L,L/v)
  A.SeingEvent(ev2)
  #print("1/g L/v="+str(( 1./g)*L/v))
  #print("2gL="+str(2*g*L))
  #print("gL/v(1+v²/c²)="+str(g*(L/v)*(1+v*v/(c*c))))
  
  # II From A, C arriving at 0
  print("=============== [III]: B and C crossing at L")
  ev3=FourVect(0,2*L/v)
  A.SeingEvent(ev3)
  
  #print("-2g L  ="+str(-2*g*L  ))
  #print(" 2g L/v="+str( 2*g*L/v))
  
  #print("2gL  ="+str(2*g*L))
  #print("2gL/v="+str(2*g*L/v))
 
  
 
  


# --------------------------------------------------------------------------
# Start the command by calling main.
# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()

 
