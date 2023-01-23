#!/usr/bin/env python3


def main():
  x=0
  v=10
  a=-1
  for t in (range(20)):
    print("x("+str(t)+")="+str(x), end=" ")
    x=x+v
    v=v+a
              
  print()
  
  
  
# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()



