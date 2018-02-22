#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import csv
import sys

fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(12, 8))

data1x, data1y, data1ye = np.loadtxt(sys.argv[1], skiprows=1, unpack=True)

axes.errorbar(data1x, data1y, yerr=data1ye)

plt.show()
