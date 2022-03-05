import csv
import numpy as np
import os
data = np.loadtxt('/home/odespo/code/bsf-ai-21/day-6/cereal.csv', dtype="str", delimiter=',', skiprows=1)

print(data.dtype)
cals = np.array(data[:, 3], dtype='int')
print(cals)