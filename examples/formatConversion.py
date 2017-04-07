#!/usr/bin/env python

"""
Convert between different types

Jens Dede, 2017, jd@comnets.uni-bremen.de
"""

floatString = "12.3"
intString   = "45"

print "Convert and add 100 to the number"
print "Convert string", floatString, "to float:", float(floatString)+100
print "Convert string", intString, "to float:", float(intString)+100
print "Convert string", intString, "to int:", int(intString)+100

print "Convert a number to a string"
print "Number:", str(123.54) + str(100)
print "Same with unicode strings:", unicode(987) + unicode(654)

# Note: If the conversion is not possible (for example from float-style string
# to int), you will raise a ValueError. Please consider catching it as
# described in exceptionHandlingExample.py
