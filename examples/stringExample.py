#!/usr/bin/env python

"""
Examples for string handling

Jens Dede, 2017, jd@comnets.uni-bremen.de
"""

s = "This is my string with some meaningful text"

print s                     # Print string
print s.split(" ")          # Separate by spaces
print s.replace("s", "x")   # Replace characters
print s.lower()             # To lower case
print s.upper()             # To upper case
print s.find("m")           # Find a character in the string
print s[:4]                 # Print part of the string

if s[:4] == "This":         # Compare strings
    print "True"
