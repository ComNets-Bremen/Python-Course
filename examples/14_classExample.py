#!/usr/bin/env python3

"""
Examples for Python classes

https://docs.python.org/3/tutorial/classes.html#a-first-look-at-classes

Jens Dede, 2019, jd@comnets.uni-bremen.de
"""

# Import class from myClassExample.py
import myClassExample

# Create an object with a specific constructor
myObject = myClassExample.helperClass("My Name")

# Use the functions provides by the class
myObject.hi()
myObject.bye()

print("The name is", myObject.getName())

# What to try out
#################
# - Check the example class "myClassExample.py" in this directory. Compare it
# with the output of this program.
# - Extend the example class: The name should be changeable using a method after
# the class got instantiated.
