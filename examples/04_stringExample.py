#!/usr/bin/env python3

"""
Examples for string handling

https://docs.python.org/3/library/string.html

Jens Dede, 2019, jd@comnets.uni-bremen.de
"""

s = "This is my string with some meaningful text"

print(s)                     # Print string
print(s.split(" "))          # Separate by spaces
print(s.replace("s", "x"))   # Replace characters
print(s.lower())             # To lower case
print(s.upper())             # To upper case
print(s.find("m"))           # Find a character in the string

# You can access parts of a string (data structure) as follows:
print(s[:4])                 # Print part of the string

# Explanation:
# s[:4]  = All characters till the 4th
# s[1:4] = Character 2 till the 4th (counting starts with 0!)
# s[-4:] = Last four characters
# s[::2] = Every 2nd character

if s[:4] == "This":         # Compare strings
    print("True")

# What to try out
#################
# - Try out how to access the different parts of the string. E.g. how to access
# every 3rd character starting from the second.
