#!/usr/bin/env python

"""
Exceptions in Python

How to deal with errors / exceptions like "File not found", "division by zero",
"conversion not possible" etc. in Python and prevent that your program crashes
for example by wrong formatted input files etc.

https://wiki.python.org/moin/HandlingExceptions

Jens Dede, 2017, jd@comnets.uni-bremen.de
"""

print 5*"*", "Catch a specific error"
try:
    print 1/0   # Division by zero not possible -> Exception
except ZeroDivisionError:   # Will catch the ZeroDivisionErrors
    print "Division by Zero catched"
    # Do whatever is necessary to solve the exception

print 5*"*", "Catch a general error"
try:
    print 2/0   # Again an exception
except:
    print "Something went wrong..."

print 5*"*", "Catch a general error with some more information"
try:
    print 3/0   # Again an exception
except Exception as e:
    print "Something went wrong and I have the following information:"
    print e

# The following line will show what happens if an error is not caught:
# Program will crash...
a = 5/"b"

# ... and the following print will never be executed
print "You will never see this message"
