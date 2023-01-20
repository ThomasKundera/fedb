#!/usr/bin/env python
import sys

name="excite".lower()


#for c in name:
  #print (c+" "+str(ord(c)-ord('a')+1))

#sys.exit(0)

def sumchar1(w):
  s=0
  for c in w:
    s+=ord(c)-ord('a')+1
  return s

def sumchar0(w):
  s=0
  for c in w:
    s+=ord(c)-ord('a')
  return s

def revsumchar1(w):
  s=0
  for c in w:
    s+=ord('z')-ord(c)+1
  return s

def revsumchar0(w):
  s=0
  for c in w:
    s+=ord('z')-ord(c)
  return s

def checkit(w):
  if ((len(w) != 6)): return
  if (sumchar(w) == 66):
    print(w)
#  else:
#    print("failed: "+w)
#    print (sumchar(w))


#with open("/usr/share/dict/french") as infile:
##  checkit("corona")
##  sys.exit(0)
  #for line in infile:
    #line=line.strip()
    #checkit(line)



# --------------------------------------------------------------------------
def main():
  phrase="Dave Ball".lower()
  sfl=[sumchar1,sumchar0,revsumchar1,revsumchar0]
  for sf in sfl:
    st=0
    print "--------"
    for word in phrase.split():
      s=sf(word)
      st+=s
      print(word+' '+str(s))
    print(st)

  


# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()
