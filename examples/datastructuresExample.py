#!/usr/bin/env python

"""
Examples using lists, tuples and dictionaries (dict)

https://docs.python.org/2.7/tutorial/datastructures.html

Jens Dede, 2017, jd@comnets.uni-bremen.de
"""

# Lists
###
print 5*"#", "Lists"
l = [1,2,3]          # List with three values

# Append some items (numbers)
l.append(12)
l.append(13)
l.append(14)
l.append(15)

# Print complete list
print "Complete list", l

# Print parts of the list
print "First entry:", l[0]
print "Last entry:", l[-1]
print "Only till the 2nd entry:", l[:2]
print "Only the last 2 entries:", l[-2:]

# Change a list item
l[1] = 123

# Lists can be sorted
l.sort()

print "Changed list:", l

# Iterate over the list
for i in l:
    print "List item", i

# Tuples
###
print "\n\n",5*"#", "Tuples"

# Create a tuple
t = (1,2,3,4,5)

# Accessing tuple items
print t, t[0], t[:-2]

# Iterate over a tuple
for i in t:
    print "Tuple item", i

# Tuples cannot be changed after assigning them!


# Dictionaries (dict) (key-value storage)
###
print "\n\n",5*"#", "Dictionaries (dict)"

data = {}   # Empty dict
data["name"] = "My Name"        # Assign value "My Name" using key "name" to dict data
data["address"] = "My Address"

# Access dict item using key
print 'data["name"]:', data["name"]

# Print complete dict
print "data:", data

# Iterate over dict
for key in data:
    print "key:", key
    print "data:", data[key]

# Init a dictionary with values
myDict = {
        "valueA": "Hallo",
        "valueB": [1,2,3,4]
        }

print myDict
print myDict["valueA"]
