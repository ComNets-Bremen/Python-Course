#!/usr/bin/env python

"""
Examples for Python classes

https://docs.python.org/2.7/tutorial/classes.html#a-first-look-at-classes

Jens Dede, 2017, jd@comnets.uni-bremen.de
"""

# Import class from myClassExample.py
import myClassExample

# Create an object with a specific constructor
myObject = myClassExample.helperClass("My Name")

# Use the functions provides by the class
myObject.hi()
myObject.bye()

print "The name is", myObject.getName()
