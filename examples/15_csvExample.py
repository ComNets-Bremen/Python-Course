#!/usr/bin/env python3

"""
Example using the csv library

https://docs.python.org/3/library/csv.html
https://docs.python.org/3/library/os.html

Jens Dede, 2019, jd@comnets.uni-bremen.de
"""

import csv
import os

# Read data from csv file

# Join the paths in an OS independent way (/ vs \)
csvfile = os.path.join("files", "noisy-dataA.csv") # Works for Windows and Linux

with open(csvfile, "r") as f:  # Open file
    csvReader = csv.reader(f)   # Treat file as csv file
    for row in csvReader:       # Iterate over all rows
        print(row)              # Print each row completely
        print(row[0])           # Print only first entry (i.e. the time column)


# Write data to csv file

with open("output.csv", "w") as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(["a","b","c"])
    csvWriter.writerow(["d","e","f"])
    csvWriter.writerow([1,2,3])

print("Output written to \"output.csv\"")
