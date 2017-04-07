#!/usr/bin/env python

"""
Examples for random numbers

https://docs.python.org/2/library/random.html

Jens Dede, 2017, jd@comnets.uni-bremen.de
"""

import random

random.seed(34) # Set the seed for the RNG

sequence = ["Apple", "Pear", "Peach", "Pineapple"]

print "Random integer between 1 and 10:", random.randint(1,10)
print "A random fruit:", random.choice(sequence)
print "A float between 0 and 1:", random.random()
print "Gaussian distribution with mu=0 and sigma=1:", random.gauss(0,1)

print "Items:", sequence
random.shuffle(sequence)
print "Shuffled items:", sequence

print "3 random elements out of the sequence:", random.sample(sequence,3)
