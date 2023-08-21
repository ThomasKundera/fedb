#!/usr/bin/env python3 

# Code base taken from:
# https://machinelearningmastery.com/simple-genetic-algorithm-from-scratch-in-python/
# We'll make it more pedantic, so to be readable

import numpy.random
import math
import string

doprint1=0 # to print sometimes only 
doprint2=0 # to print sometimes only 

#numpy.random.seed(seed=0)

def isvalid(c):
  #global doprint1
  #if (doprint1==1000):
  #  print("b: "+str(c))
  #  doprint1=0
  #doprint1+=1
  try:
    v=float(eval(c))
  except (SyntaxError, NameError, ValueError,TypeError,ZeroDivisionError,AttributeError,OverflowError) as e:
    return False
  else:
    if math. isinf(v):
      return False
    return True
  

# List of all printable ascci chars:
characters = string.ascii_letters + string.digits + string.punctuation


# Individual 
class idv:
  def __init__(self):
    self.c="1" # DNA of our species, starts with 1
    #self.muttable= [1] * 128 # table of mutation probabiliy
  
  def __str__(self):
    s="'"+str(self.c)+"' = "+str(float(eval(self.c)))
    return s

  def deepcopy(self):
    n=idv()
    n.c=self.c
    return n
  
  def mutation(self,r_mut):
    global characters
    global doprint2
    r_mut_flip   = .3
    r_mut_insert = .4
    r_mut_remove = .3
    if (len(self.c)>100):
      r_mut_insert = .001
      r_mut_remove = .999
      
    i=0
    vp=[r_mut_flip,r_mut_insert,r_mut_remove]
    
    vpn = numpy.asarray(vp).astype('float64')
    vpn = vpn / numpy.sum(vpn)
    
    #nv=math.sqrt(r_mut_flip*r_mut_flip+r_mut_insert*r_mut_insert+r_mut_remove*r_mut_remove)
    #vpn=[r_mut_flip/nv,r_mut_insert/nv,r_mut_remove/nv]
    #print ("BEGIN "+self.c)
    nc=self.c
    ncc=nc
    # To make things faster, we try several different mutations
    # as many will just not be valid syntax
    while(i<100):
      if (not (i%4)): # No more than 4 alterations in a row
        nc=ncc
      r=numpy.random.choice(3, p=vpn)
      if (r==0): # Flip
        what=numpy.random.rand()
        if (what<r_mut_flip):
          pt = numpy.random.randint(len(nc))
          xr=numpy.random.randint(128)
          c=chr(ord(nc[pt])^(xr))
          nc=nc[:pt]+c+nc[pt:]
        elif (r==1): # Insert
          pt = numpy.random.randint(len(nc))
          xr=numpy.random.choice(characters)
          nc=nc[:pt]+xr+nc[pt:]
          #try:
          #  nc=nc[:pt]+str(xr.decode("utf-8"))+nc[pt:]
          #except UnicodeDecodeError:
          #  pass
        elif (r==2): # remove
          if (len(nc)>2):
            pt = numpy.random.randint(len(nc)-2)
            nc=nc[:pt]+nc[pt+2:]
        if (isvalid(nc)):
          self.c=nc
          if (doprint2==1000):
            print("a: "+str(self)+" : "+str(onemax(self)*100))
            doprint2=0
          doprint2+=1
          return
        else:
          i+=1
          #print(str(i)+" "+nc)
      #if (i==90): print("Already 90 loops!")
    #print("ncc="+ncc+" nc="+nc+" self.c="+self.c)
    #print(str(self)+" - "+str(onemax(self)*100))
    if (not isvalid(self.c)):
      self.c='1'


# Fitness function
def onemax(idv):
  try:
    v= float(eval(idv.c))
  except:
    #print("Error string: "+str(nc))
    raise
  # Fitness is being closest to that value
  fit=2.3542e9
  return ((abs(fit-v)))


# tournament selection
def selection(pop, scores, k=3):
        # first random selection
        selection_ix = numpy.random.randint(len(pop))
        for ix in numpy.random.randint(0, len(pop), k-1):
                # check if better (e.g. perform a tournament)
                if scores[ix] < scores[selection_ix]:
                        selection_ix = ix
        return pop[selection_ix]




# crossover two parents to create two children
def crossover(p1, p2, r_cross):
        # children are copies of parents by default
        c1, c2 = p1.deepcopy(), p2.deepcopy()
        # check for recombination
        if numpy.random.rand() < r_cross:
                # select crossover point
                if (len(p1.c)>2):
                  pt = numpy.random.randint(1, len(p1.c)-1)
                  # perform crossover
                  c1.c = p1.c[:pt] + p2.c[pt:]
                  c2.c = p2.c[:pt] + p1.c[pt:]
                  #print("Mate!")
                  #print(str(p1.c)+"   "+str(p2.c))
                  #print(str(c1.c)+"   "+str(c2.c))
        return [c1, c2]
 
# genetic algorithm
def genetic_algorithm(objective, n_bits, n_iter, n_pop, r_cross, r_mut):
        # initial population of random bitstring
        pop = [idv() for _ in range(n_pop)]
        # keep track of best solution
        best, best_eval = 0, objective(pop[0])
        # enumerate generations
        for gen in range(n_iter):
                #print("genetic_algorithm(): gen: "+str(gen))
                # evaluate all candidates in the population
                scores = [objective(c) for c in pop]
                # check for new best solution
                for i in range(n_pop):
                        if scores[i] < best_eval:
                                best, best_eval = pop[i], scores[i]
                                print(">%d, new best f(%s) = %.3f" % (gen,  pop[i], scores[i]))
                # select parents
                selected = [selection(pop, scores) for _ in range(n_pop)]
                # create the next generation
                children = list()
                for i in range(0, n_pop, 2):
                        # get selected parents in pairs
                        p1, p2 = selected[i], selected[i+1]
                        # crossover and mutation
                        for c in crossover(p1, p2, r_cross):
                                # mutation
                                c.mutation(r_mut)
                                # store for next generation
                                children.append(c)
                # replace population
                pop = children
                #print ("-------------------------")
                #for p in pop:
                #  print(p)
        return [best, best_eval]
 


# --------------------------------------------------------------------------
def main():
  # define the total iterations
  n_iter = 500
  # bits
  n_bits = 20
  # define the population size
  n_pop = 500
  # crossover rate
  r_cross = .05
  # mutation rate
  r_mut = 1.0 / float(n_bits)
  # perform the genetic algorithm search
  best, score = genetic_algorithm(onemax, n_bits, n_iter, n_pop, r_cross, r_mut)
  print('Done!')
  print('f(%s) = %f' % (best, score))


# --------------------------------------------------------------------------
if __name__ == '__main__':
  main()

