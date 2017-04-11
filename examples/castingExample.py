#!/usr/bin/env python

"""
Convert between different types

Jens Dede, 2017, jd@comnets.uni-bremen.de
"""

# We use quotation marks so the numbers are actually strings: You cannot
# perform mathematical operations on it
floatString = "12.3"
intString   = "45"

print "Convert and add 100 to the number"
# with float(<string>) or int(<string>) we convert the string back to a number
print "Convert string", floatString, "to float:", float(floatString)+100
print "Convert string", intString, "to float:", float(intString)+100
print "Convert string", intString, "to int:", int(intString)+100

print "Convert a number to a string"
print "Number:", str(123.54) + str(100)

# Note: If the conversion is not possible (for example from float-style string
# to int), you will raise a ValueError. Please consider catching it as
# described in exceptionHandlingExample.py
