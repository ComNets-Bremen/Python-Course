#!/usr/bin/env python

"""
Examples for loops

Jens Dede, 2017, jd@comnets.uni-bremen.de
"""

# Print numbers from 1 to 10
print "For loop"
for number in range(1,11):
    print number

# Print numbers from 1 to 10 but break loop under certain conditions
print "Break loop"
for number in range(1,11):
    if number == 5:
        break # Stop the loop
    print number

# Print numbers from 1 to 10 but continue loop under certain conditions
print "Continue loop"
for number in range(1,11):
    if number % 2: # Modulo operator: %
        continue # Next iteration
    print number

# Iterate over items
print "Iterate loop"
items = ["Book", "Banana", "Computer"]
for item in items:
    print "I will take my", item, "with me..."

# While loop
print "While loop"
number = 1
while (number < 10):
    print number
    number += 1 # Short form for number = number + 1, number++ does not exist
