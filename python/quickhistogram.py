#!/usr/bin/python

# import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np
import csv
import sys

# fig = plt.figure()


fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(12, 8))
# ax = axes.flatten()

for i, ax in enumerate(fig.axes):
    ax.set_yscale('log')

data1x, data1y, data1ye = np.loadtxt(sys.argv[1], skiprows=1, unpack=True)
data2x, data2y = np.loadtxt(sys.argv[2], unpack=True)
data3x, data3y, data3ye = np.loadtxt(sys.argv[3], skiprows=2, unpack=True)

labels = ["Exp 1", "Exp 2", "Exp 3"]

axes.errorbar(data1x, data1y, yerr=data1ye, marker='D',
              linestyle='-',  label=labels[0])
axes.errorbar(data2x, data2y, marker='s',
              linestyle='--', label=labels[1])
axes.errorbar(data3x, data3y, yerr=data3ye, marker='p',
              linestyle='-.', label=labels[2])

plt.title("8160 GeV p+Pb, LAB frame")
plt.grid(b=True, which='major', color='gray', linestyle='--')
plt.xlabel("$\eta_{Lab}$")
plt.ylabel("$dN_{ch}/d \eta_{Lab}$")

axes.legend(bbox_to_anchor=(0.8, 0.6))

fig.tight_layout()
plt.show()
# fig.savefig("plot1.png")
# plt.close(fig)
