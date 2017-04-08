#!/usr/bin/env python

"""
Enumerate an object

Jens Dede, 2017, jd@comnets.uni-bremen.de
"""

objects = ["Apple", "Lemon", "Banana"]

for o in objects:
    print o
    # I know the object but not the position / number...

print 5*"*"

# Enumerate returns the position (i.e. an integer) and the object
for n, o in enumerate(objects):
    print "Pos", n, "Object", o
    if n==1:
        print "After second entry!!"
