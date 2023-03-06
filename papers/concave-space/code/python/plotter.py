#!/usr/bin/env python3
from math import pi, sin, cos, atan2, degrees, radians
import matplotlib.pyplot as plt



def f_beta(theta):
    return pi/2-theta

def f_fc(h,beta):
    return(h*sin(beta))

def f_fa(h,beta):
    return(h*cos(beta))

def f_fb(ab,fa):
    return(ab-fa)

def f_ah(r,theta):
    return(r*sin(theta))

def f_ab(r,theta):
    return(2*r*sin(theta))


def f_delta(fc,fb):
    return atan2(fc,fb)

def f_incidence(beta,delta):
    return(beta-delta)

def f_alpha(theta,delta):
    return(theta-delta)




def getplotdata(t0,t1,n):
    r0=6371
    r=r0-20
    h=20

    x=[]
    y=[]

    for i in range(n):
        theta=t0+i*(t1-t0)/n
        beta=f_beta(theta)
        fc=f_fc(h,beta)
        fa=f_fa(h,beta)
        ab=f_ab(r,theta)
        fb=f_fb(ab,fa)
        ah=f_ah(r,theta)
        delta=f_delta(fc,fb)
        alpha=f_alpha(theta,delta)
        incidence=f_incidence(beta,delta)
        x.append(degrees(alpha))
        y.append(degrees(incidence))
    return (x,y)

def plot(x,y):
    plt.figure(figsize=(20,12))
    plt.xlabel('alpha')
    plt.ylabel('delta')
    plt.scatter(x, y, c = 'red')
    plt.show()

def main():
    (x,y)=getplotdata(radians(1),radians(10),20)

    plot(x,y)

# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()

