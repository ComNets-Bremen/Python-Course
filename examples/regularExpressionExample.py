#!/usr/bin/env python

"""
Example using the regular expression library

https://docs.python.org/2/library/re.html

Tools:
    Evaluate regex online: https://regex101.com/
    Another webpage with lots of examples: http://www.regexr.com/
    Visual regex: https://www.debuggex.com/

Jens Dede, 2017, jd@comnets.uni-bremen.de
"""

import os
import re

logfile = os.path.join("files", "logfileA.log") # Works for Windows and Linux

# Just check the timestamp, everything else does not matter
checkTerm1 = re.compile("^At timestamp (?P<timestamp>[.?\d]+)")

# Check the complete string
checkTerm2 = re.compile("^At timestamp (?P<timestamp>[.?\d]+) we received data: valueA=(?P<valueA>\-?[.?\d]+) valueB=(?P<valueB>\-?[.?\d]+)$")

with open(logfile, "r") as f:        # Open file
    for line in f:                   # Iterate over all lines
        p = checkTerm2.match(line)   # Check if the current lines matches the expression in checkTerm
        if p:                        # If yes: Print it
            print p.group("timestamp"), p.group("valueA"), p.group("valueB")
        else:
            print 5*"#", line[:-1]   # Otherwise print the raw line (and ignore the newline at the end)
