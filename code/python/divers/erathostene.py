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


# Function to plot the triangle
def erathostene_triangle(plt,ax,dist,angle,col):
    AB=dist
    # BAC: 90-angle
    bac=d2r(90-angle)
    # BC=AB*tan()
    BC=AB*math.tan(bac)
    # AC=BC/sin()
    AC=BC/math.sin(bac)

    # Plot Point A, with label
    ax.annotate('A', (0, 0), color=col)
    ax.scatter(0, 0, color=col)
    # Plot Point B, with label
    ax.annotate('B', (AB, 0), color=col)
    ax.scatter(AB, 0, color=col)
    # Plot Point C, with label
    ax.annotate('C', (AB, BC), color=col)
    ax.scatter(AB, BC, color=col)

    # Draw triangle
    plt.plot([0, AB], [0, 0], color=col)
    plt.plot([AB, AB], [0, BC], color=col)
    plt.plot([0, AB], [0, BC], color=col)

    # Write length of line AB
    ax.annotate(str(round(AB/km))+" km", (AB/2, 0), color=col)
    # Write length of line BC
    ax.annotate(str(round(BC/km))+" km", (AB, BC/2),color=col)
    # Write length of line AC
    ax.annotate(str(round(AC/km))+" km", (AB/2, BC/2), color=col)
    print(BC)
    # Write angle
    AngleAnnotation((0, 0), (AB, BC), (0, BC), ax=ax, text=str(angle)+"°",
        textposition="outside", text_kw=dict(color=col))
    

def do_plot_test():
    fig, ax = plt.subplots()
    ax.set_xlim(-2, 10)
    ax.set_ylim(-2, 10)
    ax.set_aspect('equal')
    ax.grid()
    # Plot a thin black vertical line at origin 
    ax.plot([0,0], [0,10], color='black')
    erathostene_triangle(plt,ax, 8, 45, 'red')
    plt.show()

def do_plot():
    fig, ax = plt.subplots()
    ax.set_xlim(-20*km, 1000*km)
    ax.set_ylim(-200*km, 6500*km)
    ax.grid()
    # Plot a thin black vertical line at origin 
    ax.plot([0,0], [0,6500*km], color='black')
    erathostene_triangle(plt,ax, 800*km, 7.2, 'red')
    plt.show()


def main():
    do_plot()
    

# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()



