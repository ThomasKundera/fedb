#!/usr/bin/env python3 

# Code base taken from:
# https://machinelearningmastery.com/simple-genetic-algorithm-from-scratch-in-python/
# We'll make it more pedantic, so to be readable

import numpy.random

# Individual 
class idv:
  def __init__(self):
    self.c="1" # DNA of our species, starts with nothing
    #self.muttable= [1] * 128 # table of mutation probabiliy
  
  def __str__(self):
    i=1 # Hack for the eval
    c=1
    s="'"+str(self.c)+"' = "+str(float(eval(self.c)))
    return s

  def deepcopy(self):
    n=idv()
    n.c=self.c
    return n
  
  
  def mutation(self,r_mut):
    r_mut_flip   = .8
    r_mut_insert = .9
    r_mut_remove = 1.
    if (len(self.c)>100):
      r_mut_insert = 2.
    i=0
    nc=self.c
    # To make things faster, we try several different mutations
    # as many will just not be valid syntax
    while(i<100):
      if numpy.random.rand() < r_mut:
        what=numpy.random.rand()
        if (what<r_mut_flip):
          pt = numpy.random.randint(len(nc))
          xr=numpy.random.randint(128)
          c=chr(ord(nc[pt])^(xr))
          nc=nc[:pt]+c+nc[pt:]
        elif (what<r_mut_insert):
          pt = numpy.random.randint(len(nc))
          xr=numpy.random.bytes(1)
          try:
            nc=nc[:pt]+str(xr.decode("utf-8"))+nc[pt:]
          except UnicodeDecodeError:
            pass
        elif (what<r_mut_remove):
          if (len(nc)>2):
            pt = numpy.random.randint(len(nc)-2)
            nc=nc[:pt]+nc[pt+2:]
        try:
          v=float(eval(nc))
        except (SyntaxError, NameError, ValueError,TypeError,ZeroDivisionError,AttributeError,OverflowError) as e:
          i+=1
          #print("Error string: "+str(nc))
          pass
        else:
          self.c=nc
          return
    self.c="1"
        
    

# objective function
def onemax(idv):
  i=1 # Hack for the eval
  c=1
  try:
    v= float(eval(idv.c))
  except:
    #print("Error string: "+str(nc))
    raise
  # Fitness is being closest to 1000
  return (abs(123456789.12345678-v))
 
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
        return [c1, c2]
 
# genetic algorithm
def genetic_algorithm(objective, n_bits, n_iter, n_pop, r_cross, r_mut):
        # initial population of random bitstring
        pop = [idv() for _ in range(n_pop)]
        # keep track of best solution
        best, best_eval = 0, objective(pop[0])
        # enumerate generations
        for gen in range(n_iter):
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
        return [best, best_eval]
 
# define the total iterations
n_iter = 500
# bits
n_bits = 20
# define the population size
n_pop = 200
# crossover rate
r_cross = 0.9
# mutation rate
r_mut = 1.0 / float(n_bits)
# perform the genetic algorithm search
best, score = genetic_algorithm(onemax, n_bits, n_iter, n_pop, r_cross, r_mut)
print('Done!')
print('f(%s) = %f' % (best, score))

