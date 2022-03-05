import csv
import numpy as np
import pandas as pd
import os

print(os.chdir('./day-6'))

data = np.loadtxt('/home/odespo/code/bsf-ai-21/day-6/cereal.csv', dtype="str", delimiter=',', skiprows=1)

print(data.dtype)
cals = np.array(data[:, 3], dtype='int')
print(cals)

print()
pd_data = pd.read_csv('./cereal.csv')
fiber_data = pd_data['fiber']
fiber_data = fiber_data[0].dtype

