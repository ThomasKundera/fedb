#!/usr/bin/env python3
from math import pi, sin, cos, atan2, degrees, radians
import matplotlib.pyplot as plt

DEBUG=0

def debugprint(n,s):
    if (n<=DEBUG): print(s)

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
    if (DEBUG>=1000):
        r=1106.5
        h=204.3
        t0=radians(30)
        t1=t0
        n=1

    x=[]
    y=[]

    for i in range(n):
        theta=t0+i*(t1-t0)/n
        debugprint(1000,"theta = "+str(degrees(theta)))
        beta=f_beta(theta)
        debugprint(1000,"beta = "+str(degrees(beta)))
        fc=f_fc(h,beta)
        debugprint(1000,"fc = "+str(fc))
        fa=f_fa(h,beta)
        debugprint(1000,"fa = "+str(fa))
        ab=f_ab(r,theta)
        debugprint(1000,"ab = "+str(ab))
        fb=f_fb(ab,fa)
        debugprint(1000,"fb = "+str(fb))
        #ah=f_ah(r,theta)
        delta=f_delta(fc,fb)
        debugprint(1000,"delta = "+str(degrees(delta)))
        alpha=f_alpha(theta,delta)
        debugprint(1000,"alpha = "+str(degrees(alpha)))
        incidence=f_incidence(beta,delta)
        debugprint(1000,"i = "+str(i))
        x.append(degrees(alpha))
        y.append(degrees(incidence))
    return (x,y)

def plot(x,y):
    plt.figure(figsize=(20,12))
    plt.xlabel('Elevation angle relative to local horizon')
    plt.ylabel('Incidence angle')
    plt.plot(x, y, c = 'red',linewidth=2.0)
    plt.savefig('incidence.eps', format='eps')
    #plt.show()

def main():
    (x,y)=getplotdata(radians(1),radians(10),40)

    plot(x,y)

# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()

