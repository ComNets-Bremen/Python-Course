#!/usr/bin/env python3

"""
Examples for NumPy

http://www.numpy.org/
https://docs.scipy.org/doc/numpy/reference/

Jens Dede, 2019, jd@comnets.uni-bremen.de
"""

import numpy as np

# Array with 100 random numbers
someNumbers = np.random.random(100)

print("Some random numbers", someNumbers)

print("Sum", np.sum(someNumbers))
print("Min", np.min(someNumbers))
print("Max", np.max(someNumbers))
print("Mean", np.mean(someNumbers))
print("Median", np.median(someNumbers))

# Get 31 values between 1 and 5, evenly spaced:
print(np.linspace(1,5, num=31))

# Get Values from 0 to 10 with a step size of 0.1
print(np.arange(0, 10, 0.1))

# Some more examples
print(np.pi)
print(np.sqrt(16))
