#!/usr/bin/env python3
import datetime
import pickle

from math import sin, cos, asin, acos, pi

def d2r(d):
  return (d*pi/180)


class Airport:
  def __init__(self,iata,name,lat,lng):
    self.iata=iata
    self.name=name
    self.lat=float(lat)
    self.lng=float(lng)
    
  def __lt__(self, other):
      return hasattr(other, 'iata') and self.iata < other.iata

  def __eq__(self, other):
    return hasattr(other, 'iata') and self.iata == other.iata
  
  def __hash__(self):
    return hash(self.iata)
  
  def __str__(self):
    return(self.name+" ( "+self.iata+" )")


# Unique ID based on IATA codes.
def CreateRouteId(a):
    if (a._from<a._to):
      f=a._from.iata
      t=a._to.iata
    else:
      f=a._to.iata
      t=a._from.iata
    return (f+'_'+t)
  

class OneFlight:
  def __init__(self,fromc,to,val1,val2,day,dep,arr,nb,plane,duration):
    self._from=fromc
    self._to=to
    self._id=CreateRouteId(self)
    self._val1=val1
    self._val2=val2
    self._day=day
    self._dep=dep
    self._arr=arr
    self._nb=nb
    self._plane=plane
    
    (h,m)=duration.split(':')
    self._duration=datetime.timedelta(hours=int(h),minutes=int(m))
    
  def __str__(self):
    s="Flight"
    s+=" from "+str(self._from)
    s+=" to "+str(self._to)
    s+=" id "+str(self._id)
    s+=" val1 "+self._val1
    s+=" val1 "+self._val2
    s+=" day "+self._day
    s+=" dep "+self._dep
    s+=" arr "+self._arr
    s+=" nb "+self._nb
    s+=" plane "+self._plane
    s+=" duration "+str(self._duration)
    return s
    
  def __lt__(self, other):
      return self._duration < other._duration
  def __gt__(self, other):
      return self._duration > other._duration
  def __eq__(self, other):
      return self._duration == other._duration
  def __le__(self, other):
      return self._duration <= other._duration
  def __ge__(self, other):
      return self._duration >= other._duration
  def __ne__(self, other):
      return self._duration != other._duration


class OneRoute:
  def __init__(self,flight):
    if (flight._from<flight._to):
      self._from=flight._from
      self._to=flight._to
    else:
      self._from=flight._to
      self._to=flight._from
    self._id=CreateRouteId(flight)
    
    self._direct=[]
    self._return=[]
    
    self.GreatCircleDistance()
    
    self.AddFlight(flight)

  def AddFlight(self,flight):
    if ((self._from ==flight._from) and (self._to ==flight._to)):
      self._direct.append(flight)
    elif ((self._from ==flight._to) and (self._to ==flight._from)):
      self._return.append(flight)
    else: # This should not happens, but...
      print("ERROR in AddFlight")
      sys.exit(-1)
        
  def __lt__(self, other):
      return self._id < other._id
  def __gt__(self, other):
      return self._id > other._id
  def __eq__(self, other):
      return self._id == other._id
  def __le__(self, other):
      return self._id <= other._id
  def __ge__(self, other):
      return self._id >= other._id
  def __ne__(self, other):
      return self._id != other._id

  def SortFlights(self):
    self._direct.sort()
    self._return.sort()
    
  def GreatCircleDistance(self):
    # Compute distance using great cicle
    r_earth = 6371
    lat1=self._from.lat
    lat2=self._to.lat
    lon1=self._from.lng
    lon2=self._to.lng
    self._dist = acos(
        sin(d2r(lat1))*sin(d2r(lat2))
      + cos(d2r(lat1))*cos(d2r(lat2))*cos(d2r(lon2 - lon1))
      )*r_earth

  def ComputeTime(self):
    self.SortFlights()
    self._duration=(self._direct[0]._duration+self._return[0]._duration)/2.

  def __str__(self):
    s ="Route from :"+str(self._from)+'\n'
    s+="      to   :"+str(self._to)+'\n'
    for flight in self._direct:
      s+=str(flight)+'\n'
    s+="Route from :"+str(self._to)+'\n'
    s+="      to   :"+str(self._from)+'\n'
    for flight in self._return:
      s+=str(flight)+'\n'
    if (hasattr(self,'_duration')):
      s+="Distance: "+str(self._dist)+'\n'
      s+="Duration: "+str(self._duration)+'\n'
    return s

class SimpleRoute:
  def __init__(self,route):
    self._from=route._from
    self._to=route._to
    self._dist = route._dist
    self._duration=route._duration
    
  def __str__(self):
    s ="From "+self._from.iata+" To: "+self._to.iata
    s+=" "+"{:.0f}".format(self._dist)+" "+str(self._duration)
    return s

class AllRoutes:
  def __init__(self,flights):
    self.routes={}
    
    for flight in flights:
      if flight._id in self.routes:
        self.routes[flight._id].AddFlight(flight)
      else:
        self.routes[flight._id]=OneRoute(flight)
  
  #def Sorting(self):
  #  for route in self.routes:
  #    self.routes[route].SortFlights()
  
  def DumpData(self):
    routesdata=[]
    for route in self.routes:
      self.routes[route].ComputeTime()
      rs=SimpleRoute(self.routes[route])
      routesdata.append(rs)
      #print(self.routes[route])
      #print(rs)
    #create a pickle file
    picklefile = open('simpleroutes.dat', 'wb')
    #pickle the dictionary and write it to file
    pickle.dump(routesdata, picklefile)
    #close the file
    picklefile.close()
  
  def __str__(self):
    s=""
    for route in self.routes:
      s+="\n------------  "+str(route)+"  ------------------\n"
      s+=str(self.routes[route])+'\n'
    return s

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

  def __str__(self):
    s=""
    for flight in self.flights:
      s+='\n'+str(flight)
    s+='\n'
    return(s)

  def GenerateRoutes(self):
    self.routes=AllRoutes(self.flights)
    self.routes.DumpData()
    #self.routes.Sorting()
    #print(self.routes)
    

def main():
  flights=AllFlights()
  flights.ReadData()
  
  flights.GenerateRoutes()
  
  
  
# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()
 
