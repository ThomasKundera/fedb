#!/usr/bin/env python3

import math


def lim(f,p):
    return f(p)

def fact(n):
    if (n<=1): return 1
    return n*fact(n-1)

def exp(x):
    e=2.71828182846
    return e**x

def integrale(f,b1,b2,s):
    d=(b2-b1)/s
    itg=0.
    for i in range(int(s)):
        bi=b1+d*i
        bs=b1+d*(i+1)
        itg+=d*(f(bi)+f(bs))/2.
        #        print(str(i)+" "+str(itg)+" "+str(bi)+" "+str(bs))
    return itg

def tsum(f,m,M):
    s=0
    for i in range(m,M):
        s+=f(i)
    return s

def A(n):
    return ( ( (2.**(2*n)) * (fact(n)**2) * (math.log(7)) )\
        / (fact(2*n)*math.sqrt(n)) )

def A1(p):
    a=lim(A11,p)
    print ("A1="+str(a))
    return a


def A21(p):
    return exp(-p*p)

def A2(p):
    a=integrale(A21,0,p,p*2)
    print ("A2="+str(a))
    return a

def A(p):
    a=exp(A1(p)/A2(p))
    print ("A="+str(a))
    return a


def B111(n):
    return(8./((4*n+1)*(4*n+3)))

def B11(p):
    return tsum(B111,0,2*p)

def B(p):
    a=math.cos(B11(p))
    print ("B="+str(a))    
    return a


def Ftest(x):
  if (x<1): return 1-x
  else: return 0

def C1(x):
  return (3./((x**6)+1))


def C(p):
    a=integrale(C1,0,p,p*p)
    print ("C="+str(a))    
    return a

def B1(p):
  return fact(4*p)

def B2(p):
  return (1103+26390*p)

def B3(p):
  b31=fact(p)
  return b31**4

def B4(p):
  return 396**(4*p)

def B0(p):
    return ((B1(p)*B2(p))/(B3(p)*B4(p)))

def B(p):
  return tsum(B0,0,30)
    

def tout(p):
    a=math.sqrt(8)/9801
    b=B(p)
    print (str(a)+"  "+str(b))
    return (a*b)

# --------------------------------------------------------------------------
def main():
  print (str(1./math.pi))
  for p in range(1,5):
    print ("p: "+str(p)+" Val= "+str(tout(p)))

  


# --------------------------------------------------------------------------
# Start the command by calling main.
# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()

 
