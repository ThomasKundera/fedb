#!/usr/bin/env python3 


def main():
  for a in range(1,100):
    for b in range(1,100):
      for c in range(1,100):
        s=a*a+b*b+c*c
        if (abs(s-10000)<2):
          print(str(s)+": "+str(a)+" "+str(b)+" "+str(c))

# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()
