#!/usr/bin/env python

"""
Examples for the usage of pickles in Python

https://docs.python.org/2/library/pickle.html

Jens Dede, 2017, jd@comnets.uni-bremen.de
"""

import pickle

complexStructure = {
        "dataA": [1,2,3,4,5],
        "dataB": [9,9,9,8,7],
        "dataC": "This is my text"
        }

# Store the dictionary "complexStructure" into the file "dataExport.pickle"
with open("dataExport.pickle", "wb") as f:
    pickle.dump(complexStructure, f)


# In another script...
data = None # Initialize variable here to make it accessible outside the "with" block (scope)
with open("dataExport.pickle", "rb") as f:
    data = pickle.load(f)

print data
print data["dataC"]


