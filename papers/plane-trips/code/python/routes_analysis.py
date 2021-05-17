#!/usr/bin/env python3
import pickle
from flight_data import SimpleRoute
import matplotlib.pyplot as plt


class RoutesAnalysis:
  def __init__(self,routes):
    self.routes=routes
    
  def SimplePlot(self):
    # Just plot distance vs time
    x=[]
    y=[]
    for route in self.routes:
      x.append(route._duration.total_seconds())
      y.append(route._dist)
      
    plt.scatter(x, y, c = 'red')
    plt.xlabel('Time of flight (s)')
    plt.ylabel('Distance of flight (km)')
    plt.show()

def main():
  #read the pickle file
  picklefile = open('simpleroutes.dat', 'rb')
  #unpickle the dataframe
  routes = pickle.load(picklefile)
  #close file
  picklefile.close()
  ra=RoutesAnalysis(routes)
  ra.SimplePlot()
  

  
  
# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()
