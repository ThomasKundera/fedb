#!/usr/bin/env python3
import sys
import re
import difflib
import datetime
import csv
from html.parser import HTMLParser

import flight_data

from enum import Enum, auto
class kOWR_states(Enum):
  start     =auto()
  indiv     =auto()
  indata    =auto()
  infillline=auto()
  outdiv    =auto()
 
 
def AirCode(s):
  r=s[::-1].split(')')
  if (len(r)<=1):
    print("ERROR: invalid Airport Code")
    return None
  ac=r[1].split('(')
  return(ac[0][::-1])


class OneWorldReader(HTMLParser):
  def __init__(self,airports):
    super().__init__()
    self.airports=airports
    self.flights=flight_data.AllFlights()
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
          self.twotrips=True
          iata=AirCode(self.tablefromto[2])
          print(iata)
          self.fromairport=self.airports[iata] #Airport(self.tablefromto[2])
          iata=AirCode(self.tablefromto[7].split(':')[1].strip())
          self.destairport=self.airports[iata] #Airport(self.tablefromto[7].split(':')[1].strip())
        else:
          self.twotrips=False
          iata=AirCode(self.tablefromto[2])
          self.fromairport=self.airports[iata] #Airport(self.tablefromto[2])
          iata=AirCode(self.tablefromto[3].split(':')[1].strip())
          self.destairport=self.airports[iata] #Airport(self.tablefromto[3].split(':')[1].strip())
 
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
    direct=True
    for item in items:
      joinitems+=s.join(item)+" "
      if (direct):
        afrom=self.fromairport
        ato=self.destairport
      else:
        ato=self.fromairport
        afrom=self.destairport
      self.flights.Add(flight_data.OneFlight(afrom,ato,
                                            item[0],item[1],item[2],
                                            item[3],item[4],
                                            item[5],item[6],item[7]))
      if self.twotrips:
        direct=not direct
      print(self.flights.flights[-1])
    # test
    splitdata=self.dataline.split()
    joindata=s.join(splitdata)
    #print(joindata)
    #print(joinitems)
    return
    # This is supposed to test regexpr efficiency, but for some reason
    # doesn't work. FIXME
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


class AirPortDBReader:
  def __init__(self,fn):
    self.airports={}
    fi=open(fn,"rt",newline='')
    reader=csv.reader(fi)
    for row in reader:
      #res=line.split(',')
      # "id","ident","type","name","latitude_deg","longitude_deg","elevation_ft",
      #  0    1       2      3      4              5               6
      #"continent","iso_country","iso_region","municipality","scheduled_service",
      # 7           8             9            10             11
      #"gps_code","iata_code","local_code","home_link","wikipedia_link","keywords"
      # 12         13          14           15          16               17
      #print(res[4])
      iata=row[13]
      if (len(iata)>2 and len(iata)<5): # Ignoring airports without IATA
                                        #FIXME: that's local code?
        # IATA name lat long
        self.airports[iata]=flight_data.Airport(iata,row[3],row[4],row[5])
    fi.close()
    #for airp in self.airports:
    #  print (airp)
    #sys.exit(0)
    

def main():
  airDb = AirPortDBReader("../../data/airports.csv")
  parser = OneWorldReader(airDb.airports)
  fi=open("../../data/oneworlds-div.html","rt")
  data=fi.read()
  parser.feed(data)
  fi.close()
  
  #allflights=parser.flights
  
  #sortedflights=sorted(allflights)
  
  #for flight in sortedflights:
  #  if ((flight.fromc.lat>0) and (flight.to.lat>0)): # Only nothern hemisphere
  #    print(flight)

  
# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()

