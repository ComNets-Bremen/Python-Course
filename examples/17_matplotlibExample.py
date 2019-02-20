#!/usr/bin/env python3

"""
Example using matplotlib

http://matplotlib.org

Jens Dede, 2019, jd@comnets.uni-bremen.de
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 4*np.pi, 0.1) # 0, 0.1, 0.2, ... 4*pi-0.1)

figure = plt.figure(figsize=(12, 6)) # size of resulting figure in inches
ax = figure.add_subplot(111) # Add just one single subplot

ax.plot(x, np.sin(x), label="My Data A")    # 1st plot
ax.plot(x, np.sin(x*2), label="My Data B")  # 2nd plot

ax.legend(loc='best') # We would like to have a legend
ax.grid(True)   # Show grid

plt.tight_layout()  # Fit everything to less space

plt.savefig("output.pdf")   # Save result into file (pdf, png, jpg etc.)
plt.show()  # Show the result on the screen

