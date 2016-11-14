#!/usr/bin/env python

import sys
import datetime
import math
import geographiclib


# A UTC class.
class UTC(tzinfo):
    ZERO = timedelta(0)
    HOUR = timedelta(hours=1)
    """UTC"""
    def utcoffset(self, dt):
        return ZERO
    def tzname(self, dt):
        return "UTC"
    def dst(self, dt):
        return ZERO


# Location point
class Wsg84Point:
  def __init__(self,lat,lng):
    self.lat=lat
    self.lng=lng
    

# All points close enough will be considered as same and be attribued an ID
# should be a singleton, for now using a global
locid_dict={}
locid_max=0
def set_locid(loc):
  for locid, loc in locid_dict.iteritems():
    

class LocIds:
  def __init__(self):
    
 

class Event:
  def __init__(self,userid=0,evdate=datetime.now(UTC()),evloc=Wsg84Point(0,0),lM,l,a):
    self.userid   =userid
    self.evdate   =evdate
    self.evlocid  =locid(loc)
    self.elevation=math.atan(l/lM)
    self.azimuth  =a
    
  def locid(loc):
    
    


def main():
  return
  
# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()

