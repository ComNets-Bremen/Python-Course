#!/usr/bin/env python

"""
Examples for the usage of json in Python

https://docs.python.org/2/library/json.html

Jens Dede, 2017, jd@comnets.uni-bremen.de
"""

import json

complexStructure = {
        "dataA": [1,2,3,4,5],
        "dataB": [9,9,9,8,7],
        "dataC": "This is my text"
        }


print "Original structure:", complexStructure

print "json formatted structure:", json.dumps(complexStructure)

# backslash (\): line continues next line
print "Nicer formatted json:", \
        json.dumps(
            complexStructure,
            sort_keys=True,
            indent=4,
            separators=(',', ': ')
            )

# Write to file
with open("file.json", "w") as jsonOutput:
    jsonDump = json.dumps(
            complexStructure,
            sort_keys=True,
            indent=4,
            separators=(',', ': ')
            )
    jsonOutput.write(jsonDump)

