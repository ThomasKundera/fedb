#!/usr/bin/env python3
import pickle
from flight_data import SimpleRoute
import scipy.stats
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
  
    a, b, r_value, p_value, std_err = scipy.stats.linregress(x,y)
    print ( "Distance (km) = "   +"{:.2f}".format(a)
           +" x Time (secondes) "+"{:.0f}".format(b)
           +" ( {:.6f}".format(p_value)+"- {:.6f}".format(std_err)+" )")
    yp=[]
    for xv in x:
      yp.append(a*xv+b)

    plt.scatter(x, y, c = 'red')
    plt.plot   (x, yp , color='blue',linewidth=3)
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
