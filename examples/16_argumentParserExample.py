#!/usr/bin/env python3

"""
Example using the argument parser

https://docs.python.org/3/library/argparse.html

Jens Dede, 2019, jd@comnets.uni-bremen.de
"""

import argparse

parser = argparse.ArgumentParser(description='Example Parser')

# The filename has to be given
parser.add_argument('filename', metavar='file', type=str, help='The filename to process')

# A number might be given. If not used, set it to "None"
parser.add_argument('-n', metavar="number", type=int, default=None, help="A number option which can be empty")

# Boolean value which is false per default and true if set on the command line
parser.add_argument('-l', action='store_true', default=False, help="Enable logging")

args = parser.parse_args()

print("Filename", args.filename)
print("Number", args.n)
print("Logging", args.l)

# What to try out
#################
# Check the documentation of the argument parser. How to add all number given
# as an argument?
