#!/usr/bin/env python3
from html.parser import HTMLParser

from enum import Enum, auto
class kOWR_states(Enum):
  start     =auto()
  indiv     =auto()
  indata    =auto()
  infillline=auto()
  outdiv    =auto()
 
 
def AirCode(s):
  r=s.split('(')
  if (len(r)<=1):
    print("ERROR: invalid Airport Code")
    return None
  ac=r[1].split(')')
  return(ac[0])
   
   
class Airport:
  def __init__(self,name):
    self.name=name
    self.code=AirCode(name)
    
  def __eq__(self, another):
    return hasattr(another, 'name') and self.name == another.name
  
  def __hash__(self):
    return hash(self.name)
  
  def __str__(self):
    return(self.name+" - "+self.code)
    
class OneFlight:
  def __init__(self,fromc,to,val1,val2,day,dep,arr,nb,plane,duration):
    self.fromc=fromc
    self.to=to
    self.val1=val1
    self.val2=val2
    self.day=day
    self.dep=dep
    self.arr=arr
    self.nb=nb
    self.plane=plane
    self.duration=duration
    
  def __str__(self):
    s="Flight"
    s+=" from "+str(self.fromc)
    s+=" to "+str(self.to)
    s+=" val1 "+self.val1
    s+=" val1 "+self.val2
    s+=" day "+self.day
    s+=" dep "+self.dep
    s+=" arr "+self.arr
    s+=" nb "+self.nb
    s+=" plane "+self.plane
    s+=" duration "+self.duration
    return s
    

class OneWorldReader(HTMLParser):
  def __init__(self):
    super().__init__()
    self.flights=[]
    self.state=kOWR_states.start
    self.cnt=0
  
  def handle_starttag(self, tag, attrs):
    if (self.state == kOWR_states.indata):
      print("Encountered a start tag:", tag)
    if (tag == 'div'):
      if (self.state == kOWR_states.start):
        self.cnt+=1
        if (self.cnt == 4):
          self.state = kOWR_states.indiv
          self.cnt=0
      else:
        self.state = kOWR_states.indiv
    
  def handle_endtag(self, tag):
    if (self.state == kOWR_states.indata):
      print("Encountered an end tag :", tag)
    if (tag == 'div'):
      if (self.state == kOWR_states.indata) or (self.state == kOWR_states.infillline):
        self.state = kOWR_states.outdiv
        self.cnt=0
    
  def handle_data(self, data):
    if (self.state == kOWR_states.indiv):
      self.cnt+=1
      if (self.cnt == 3):
        self.cnt2=0
        self.fromairport=Airport(data.strip())
        print("From airport: "+str(self.fromairport))
      elif (self.cnt == 8):
        self.destairport=Airport(data. split(':')[1].strip())
        print("Destination: "+str(self.destairport))
      elif (data.strip() == "Aircraft time"): #self.cnt == 41):
        self.cnt2+=1
        if (self.cnt2==2):
          self.state = kOWR_states.indata
          self.cnt=self.cnt2=0
          print("---------- data starts -------")
    elif (self.state == kOWR_states.indata):
      self.cnt+=1
      print("Counter (indata): "+str(self.cnt))
      if   ((self.cnt==1) or (self.cnt==1+7)):
        if ("Operated" in data):
          self.state = kOWR_states.infillline
          print("Fill line:"+data.strip())
          self.cnt=0
          return
        self.val1=data.strip()
        print("val1: "+self.val1)
        
      elif (self.cnt==2) or (self.cnt==2+7):
        self.val2=data.strip()
        print("val2: "+self.val2)
        
      elif (self.cnt==3) or (self.cnt==3+7):
        self.day=data.strip()
        print("day: "+self.day)
        
      elif (self.cnt==5) or (self.cnt==5+7):
        data=data.split()
        self.dep=data[0].strip()
        self.arr=data[1].strip()
        print("dep: "+self.dep)
        print("arr: "+self.arr)
         
      elif (self.cnt==6) or (self.cnt==6+7):
        data=data.split()
        self.nb=data[0].strip()
        self.plane=data[1].strip()
        print("nb: "+self.nb)
        print("plane: "+self.plane)
        
      elif (self.cnt==7):
        self.duration=data.strip()
        print("Trip duration: "+self.duration)
        self.flights.append(OneFlight(self.fromairport,self.destairport,
                                      self.val1,self.val2,self.day,
                                      self.dep,self.arr,
                                      self.nb,self.plane,self.duration))
        print(self.flights[-1])
      elif (self.cnt==14): # Return trip
        self.duration=data.strip()
        print("Trip duration: "+self.duration)
        self.flights.append(OneFlight(self.destairport,self.fromairport, # Inverted to/from
                                      self.val1,self.val2,self.day,
                                      self.dep,self.arr,
                                      self.nb,self.plane,self.duration))
        print(self.flights[-1])
        self.cnt=0 # Going to next line
    elif (self.state == kOWR_states.infillline):
      self.cnt+=1
      print("Counter(infillline): "+str(self.cnt))
      if (self.cnt == 1):
        self.state = kOWR_states.indata
        self.cnt=0
        
    if (self.state == kOWR_states.indata) or (self.state == kOWR_states.infillline):
      print("Encountered some data  :", data)

        




def main():
  parser = OneWorldReader()
  fi=open("../../data/oneworlds-div.html","rt")
  data=fi.read()
  parser.feed(data)

  
# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()

