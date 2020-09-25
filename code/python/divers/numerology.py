#!/usr/bin/env python
import sys

name="excite".lower()


for c in name:
  print (c+" "+str(ord(c)-ord('a')+1))

sys.exit(0)

def sumchar(w):
  s=0
  for c in w:
    s+=ord(c)-ord('a')+1
  return s

def checkit(w):
  if ((len(w) != 6)): return
  if (sumchar(w) == 66):
    print(w)
#  else:
#    print("failed: "+w)
#    print (sumchar(w))


with open("/usr/share/dict/french") as infile:
#  checkit("corona")
#  sys.exit(0)
  for line in infile:
    line=line.strip()
    checkit(line)
