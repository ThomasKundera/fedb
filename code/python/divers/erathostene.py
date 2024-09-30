#!/usr/bin/env python3
import sys
import math
from math import pi
import matplotlib.pyplot as plt
from angle_notation import AngleAnnotation

sys.path.insert(0, '../common')
km=1

# convert from degrees to radians
def d2r(d):
    return d*(pi/180)



def main():
    # ABC triangle
    # AB=800km
    AB=800*km
    # BAC: 90-7.2°
    bac=d2r(90-7.2)
    # BC=AB*tan(90-7.2°)
    BC=AB*math.tan(bac)
    # Remove decimals for print
    print("BC="+str(BC/km).split(".")[0]+" km")
    
    fig, ax = plt.subplots()
    ax.set_xlim(-20*km, 1000*km)
    ax.set_ylim(-200*km, 6500*km)
    # Plot Point A, with label
    ax.annotate('A', (0, 0))
    ax.scatter(0, 0, color='red')
    # Plot Point B, with label
    ax.annotate('B', (AB, 0))
    ax.scatter(AB, 0, color='red')
    # Plot Point C, with label
    ax.annotate('C', (AB, BC))
    ax.scatter(AB, BC, color='red')

    # 

    # Plot line AB
    ax.plot([0,AB], [0,0], color='red')
    # Write length of line AB
    ax.annotate(str(AB/km).split(".")[0]+" km", (AB/2, -10*km))

    # Plot line BC
    ax.plot([AB,AB], [0,BC], color='red')
    # Plot line AC
    ax.plot([0,AB], [0,BC], color='red')
    # Plot a thin black vertical line at origin 
    ax.plot([0,0], [0,6500*km], color='black')
    
    # Add angle annotation
    AngleAnnotation((0, 0), (AB, BC), (0, 1000*km), ax=ax, text="7.2°", textposition="inside")  

    plt.show()


  
  
  
# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()



