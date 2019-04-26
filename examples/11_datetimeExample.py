#!/usr/bin/env python3

"""
Example for date and time handling


https://docs.python.org/3/library/datetime.html
https://docs.python.org/3/library/time.html
https://pypi.python.org/pypi/parse


Jens Dede, 2019, jd@comnets.uni-bremen.de
"""
import time
import datetime
from dateutil import parser

print("Linux Timestamp:", time.time())
print("Now:", datetime.datetime.now())

print("Year:", datetime.datetime.now().year)
print("Hour:", datetime.datetime.now().hour)

print("Parsed time format 1:", parser.parse("Oct 12 2001 11:56:11AM"))
print("Parsed time format 2:", parser.parse("24.12.2016 14:03"))
print("Parsed time format 3:", parser.parse("11:03"))

print("Datetime from timestamp:", datetime.datetime.fromtimestamp(1010101010.10))

newYear = datetime.datetime(2019, 1, 1)
print("New year", newYear)

# What to try out
#################
# - You can also calculate with times. Try it out!
