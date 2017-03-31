#!/usr/bin/env python

"""
Examples for functions

https://docs.python.org/2.7/tutorial/controlflow.html#defining-functions

Jens Dede, 2017, jd@comnets.uni-bremen.de
"""


def addNumbers(numberA, numberB):
    """
    Functions should be always documented with such a "Doxygen"-comment
    """
    return numberA + numberB


print "1 + 4 =", addNumbers(1,4)


def greeting(name="Nobody"):
    """
    Greets the person. Uses "Nobody" if no name is given
    """
    return "Hi " + name + "!"

print "Greeting without argument:", greeting()
print "Greeting with argument:", greeting("John Doe")
