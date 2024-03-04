#!/usr/bin/env python3
import json

def main():
  f = open('simpletest2.json')
  data= json.load(f)
  print(data)
  
# --------------------------------------------------------------------------
if __name__ == '__main__':
        main()
        
        
