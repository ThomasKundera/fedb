#!/usr/bin/env python3
import sys
import re
import difflib
import datetime
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
    
    (h,m)=duration.split(':')
    self.duration=datetime.timedelta(hours=int(h),minutes=int(m))
    
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
    s+=" duration "+str(self.duration)
    return s
    
  def __lt__(self, other):
      return self.duration < other.duration
  def __gt__(self, other):
      return self.duration > other.duration
  def __eq__(self, other):
      return self.duration == other.duration
  def __le__(self, other):
      return self.duration <= other.duration
  def __ge__(self, other):
      return self.duration >= other.duration
  def __ne__(self, other):
      return self.duration != other.duration

class OneWorldReader(HTMLParser):
  def __init__(self):
    super().__init__()
    self.flights=[]
    self.state=kOWR_states.start
    self.cnt=0
  
  def handle_starttag(self, tag, attrs):
    #if (self.state == kOWR_states.indata):
    #  print("Encountered a start tag:", tag)
    if (tag == 'div'):
      print("------------ div -------------")
      if (self.state == kOWR_states.start):
        self.cnt+=1
        if (self.cnt == 4):
          self.state = kOWR_states.indiv
          self.cnt=0
          self.tablefromto=[]
      else:
        self.state = kOWR_states.indiv
        self.cnt=0
        self.tablefromto=[]
        
  def handle_endtag(self, tag):
    #if (self.state == kOWR_states.indata):
    #  print("Encountered an end tag :", tag)
    if (tag == 'div'):
      if (self.state == kOWR_states.indata) or (self.state == kOWR_states.infillline):
        self.state = kOWR_states.outdiv
        self.cnt=0
        self.parse_dataline()
        
  def handle_data(self, data):
    if (self.state == kOWR_states.indiv):
      self.cnt+=1
      self.tablefromto.append(data.strip())
      
      if (data.strip() == "Aircraft time"):
        self.state = kOWR_states.indata
        # FIXME : we'll get junk data when 2 tables (that should be ignored hopefully)
        #print("TABLE: "+str(self.cnt))
        #print(self.tablefromto)
        if (self.cnt>21): # Two tables
          self.fromairport=Airport(self.tablefromto[2])
          self.destairport=Airport(self.tablefromto[7].split(':')[1].strip())
        else:
          self.fromairport=Airport(self.tablefromto[2])
          self.destairport=Airport(self.tablefromto[3].split(':')[1].strip())
        #print(self.fromairport)
        #print(self.destairport)
        self.cnt=0
        self.dataline=""
          #print("---------- data starts -------")
    elif (self.state == kOWR_states.indata):
      self.dataline+=" "+data.strip()
        
    #print("Encountered some data  :", data)

  
  def parse_dataline(self):
    #     -     - 12 4 6 07:50 09:05    S7124   319 05:15
    #     -     - 1 3 5 7 22:00 06:35+1 S7123   319 04:35 
    #     - 18Nov 1234567 05:50 06:40   AA2734* ERD 00:50 
    #     - 16Nov 123 567 09:35 10:25   AA2898* ER4 00:50 
    # 20Nov -      1 45 7 05:50 06:40   AA2734* ERD 00:50 
    # 17Nov -     1234567 09:45 10:35   AA2898* ERD 00:50
    # 19Nov -           6 06:30 07:20   AA2734* ERD 00:50 
    # 17Nov -     1234567 12:15 13:05   AA2729* ER3 00:50
    # 17Nov -     12345 7 06:35 07:25   AA2940* ER4 00:50
    #     - -     12345 7 12:55 15:45   BA8217* FRJ 01:50
    print ("---------------------------------------------------------")
    print("DATA: "+self.dataline)
    self.dataline=re.sub('\s+', ' ', self.dataline)
    retem = re.compile(
      "\s+(-|[0-9]{1,2}[A-Z][a-z][a-z])"+              # val1
      "\s+(-|[0-9]{1,2}[A-Z][a-z][a-z])"+              # val2
      "\s+([0-7\s]+)"+                                 # day
      "\s+([0-9][0-9]:[0-9][0-9])"+                    # dep
      "\s+([0-9][0-9]:[0-9][0-9])"+"(?:\+[0-9]+){0,1}" # arr
      "\s+([\w\*]+)"+                                  #
      "\s+(\w+)"+                                      #
      "\s+([0-9][0-9]:[0-9][0-9])"                     #
      )
    items=retem.findall(self.dataline)
    s=" "
    joinitems=""
    direct=True # FIXME: this is invalid: if there are not as many from than to
    for item in items:
      joinitems+=s.join(item)+" "
      if (direct):
        afrom=self.fromairport
        ato=self.destairport
      else:
        ato=self.fromairport
        afrom=self.destairport
      self.flights.append(OneFlight(afrom,ato,
                                    item[0],item[1],item[2],
                                    item[3],item[4],
                                    item[5],item[6],item[7]))
      direct=not direct
      print(self.flights[-1])
    # test
    splitdata=self.dataline.split()
    joindata=s.join(splitdata)
    #print(joindata)
    #print(joinitems)
    matches = difflib.SequenceMatcher(None,joindata , joinitems).get_matching_blocks()
    ptr=0
    for match in matches:
      print("Matching: "+str(match.a)+" "+str(match.a+match.size))
      if ("-" in joindata[ptr:match.a]):
        print("ERROR: "+str(ptr)+" "+str(match.a))
        print(joindata[ptr:match.a])
        print("--")
        print(joindata)
        print("--")
        print(joinitems)
        print("----")
        for item in items:
          print (item)
        #sys.exit(0) FIXME: errors shouldn't be ignored
      ptr=match.a + match.size
    
    

def main():
  parser = OneWorldReader()
  fi=open("../../data/oneworlds-div.html","rt")
  data=fi.read()
  parser.feed(data)
  
  allflights=parser.flights
  
  sortedflights=sorted(allflights)
  
  for flight in sortedflights:
    print(flight)

  
# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()

