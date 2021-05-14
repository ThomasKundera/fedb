#!/usr/bin/env python3
from html.parser import HTMLParser

from enum import Enum, auto
class kOWR_states(Enum):
  start =auto()
  indiv =auto()
  indata=auto()
 

class OneCity:
  def __init__(self,name):
    self.name=name
    print("New city named "+name)
    

class OneWorldReader(HTMLParser):
  def __init__(self):
    super().__init__()
    self.cities={}
    self.state=kOWR_states.start
    self.cnt=0
  
  def handle_starttag(self, tag, attrs):
    if (self.state != kOWR_states.indata):
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
    if (self.state != kOWR_states.indata):
      print("Encountered an end tag :", tag)
      
  def handle_data(self, data):
    if (self.state == kOWR_states.indiv):
      self.cnt+=1
      print("Counter: "+str(self.cnt))
      if (self.cnt == 3):
        # FIXME : If city exists, escape
        fromcity=data.strip()
        self.cities[fromcity]=OneCity(fromcity)
      elif (self.cnt == 8):
        print(data)
        # FIXME : If city exists, escape
        self.destcity=data. split(':')[1].strip()
        print("Destination: "+self.destcity)
      elif (self.cnt == 42):
        self.state = kOWR_states.indata
        print("---------- data starts -------")
        
    if (self.state != kOWR_states.indata):
      print("Encountered some data  :", data)
          




def main():
  parser = OneWorldReader()
  fi=open("../../data/oneworlds-div.html","rt")
  data=fi.read()
  parser.feed(data)

  
# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()

