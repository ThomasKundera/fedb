#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Simulation of ballistic trajectory on 
# - flat plane
# - globe
# - concave Earth
# Taking into account:
# - atmosphere (and atmospheric gradiant)
# Ignoring:
# - Earth self-rotation


import sys
sys.path.insert(0, '../common')

import math
from tkunits import m, km, dg, pi, g_earth

def simple_free_fall(h):
    t = math.sqrt(2 * h / g_earth)
    return t  # Returns time in seconds as a float

def main():
  print(simple_free_fall(400*m))

# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()



