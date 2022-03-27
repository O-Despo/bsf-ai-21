#Statistics with numpy
import math
import numpy as np
from numpy.random import default_rng
from pandas import array

#The mean (average)
line_data = np.linspace(0,10)

z = 0
for n in line_data:
    z += n

line_data_mean = z/len(line_data)

print(line_data.mean())

#The Mode (the number that apears the most)
line_data = np.concatenate((np.arange(0,10), np.arange(6,8)))
print(line_data)
vals, counts = np.unique(line_data, return_counts=True)
mode = vals[np.nonzero(counts == counts.max())]

# Median (one in the middle)
len_d2 = len(line_data)/2

if len(line_data)%2 == 0:
    med = line_data[int(len_d2) - 1]
else:
    med = (line_data[math.floor(len_d2) - 1] + line_data[round(len_d2) - 1])/2

print(f"median: {med}")

#Range
range_line_data = (line_data.min(), line_data.max())

#Proportion
prop = len(np.nonzero(line_data == 8))/len(line_data)
print(prop)
#Numpy calls from the standard normal distribution1
rng = default_rng()
vals = rng.standard_normal(10)

print(vals)
