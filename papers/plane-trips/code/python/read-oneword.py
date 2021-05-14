#!/usr/bin/env python3
from html.parser import HTMLParser

from enum import Enum, auto
class kOWR_states(Enum):
  start =auto()
  indiv =auto()
  indata=auto()
 
 
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
    


class OneCity:
  def __init__(self,name):
    self.name=name
    print("New city named "+name)
    self.flights={}
    
  def AddFlight(self,dest,val1,val2,day,dep,arr,nb,plane,duration):
    if (dest not in self.flights):
      self.flights[dest]=[]
    self.flights[dest].append(OneFlight(self.name,dest,val1,val2,day,dep,arr,nb,plane,duration))
    
    

class OneWorldReader(HTMLParser):
  def __init__(self):
    super().__init__()
    self.cities={}
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
      
  def handle_data(self, data):
    if (self.state == kOWR_states.indata):
      print("Encountered some data  :", data)

    if (self.state == kOWR_states.indiv):
      self.cnt+=1
      if (self.cnt == 3):
        self.fromcity=data.strip()
        print("From city: "+self.fromcity)
      elif (self.cnt == 8):
        self.destcity=data. split(':')[1].strip()
        print("Destination: "+self.destcity)
      elif (self.cnt == 41):
        self.state = kOWR_states.indata
        self.cnt=0
        print("---------- data starts -------")
    elif (self.state == kOWR_states.indata):
      self.cnt+=1
      print("Counter: "+str(self.cnt))
      if   (self.cnt==1):
        self.val1=data.strip()
      elif (self.cnt==2):
        self.val2=data.strip()
      elif (self.cnt==3):
        self.day=data.strip()
      elif (self.cnt==5):
        print("--5--"+data)
        data=data.split()
        print(data)
        self.dep=data[0].strip()
        self.arr=data[1].strip()
      elif (self.cnt==6):
        
        print("--6--"+data)
        data=data.split()
        print(data)
        #sys.exit(0)
        self.nb=data[0].strip()
        self.plane=data[1].strip()
      elif (self.cnt==8):
        self.duration=data.strip()
        print("Trip duration: "+self.duration)
        # FIXME : If city exists, escape
        if (self.fromcity not in self.cities):
          self.cities[self.fromcity]=OneCity(self.fromcity)
        self.cities[self.fromcity].AddFlight(self.destcity,self.val1,self.val2,self.day,self.dep,self.arr,self.nb,self.plane,self.duration)
        




def main():
  parser = OneWorldReader()
  fi=open("../../data/oneworlds-div.html","rt")
  data=fi.read()
  parser.feed(data)

  
# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()

