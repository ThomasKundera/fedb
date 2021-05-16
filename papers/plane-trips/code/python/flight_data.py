#!/usr/bin/env python3
import datetime
import pickle

class Airport:
  def __init__(self,iata,name,lat,lng):
    self.iata=iata
    self.name=name
    self.lat=float(lat)
    self.lng=float(lng)
    
  def __eq__(self, another):
    return hasattr(another, 'iata') and self.iata == another.iata
  
  def __hash__(self):
    return hash(self.iata)
  
  def __str__(self):
    return(self.name+" ( "+self.iata+" "+str(self.lat)+" )")


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

class AllFlights:
  def __init__(self):
    self.flights=[]
  def Add(self,f):
    self.flights.append(f)
    
  def DumpData(self):
    #create a pickle file
    picklefile = open('allflights.dat', 'wb')
    #pickle the dictionary and write it to file
    pickle.dump(self.flights, picklefile)
    #close the file
    picklefile.close()
    
  def ReadData(self):
    #read the pickle file
    picklefile = open('allflights.dat', 'rb')
    #unpickle the dataframe
    self.flights = pickle.load(picklefile)
    #close file
    picklefile.close()
    
  
