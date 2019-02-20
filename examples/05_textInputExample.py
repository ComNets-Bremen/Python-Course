#!/usr/bin/env python3

"""
Text input examples

https://docs.python.org/3/library/functions.html#input
https://docs.python.org/3/library/functions.html#eval

Jens Dede, 2019, jd@comnets.uni-bremen.de
"""

# Text input
name = input("Please enter your name:")
print("Hi,",name)

# Number input
number = eval(input ("Please enter a number:"))
print("Here are your numbers:", list(range(number))) # Print range of numbers
