import csv
from enum import unique
from operator import mod
import numpy as np
import pandas as pd
import os
import statistics

print(os.getcwd())

#Pandas vs Numpy
data = np.loadtxt('./day-6/cereal.csv', dtype="str", delimiter=',', skiprows=1)

print(data.dtype)
cols = np.array(data[:, 3], dtype='int')
print(cols)

def get_mode(arr):
    unique, count = np.unique(fiber_data, return_counts=True) 
    modes = unique[np.nonzero(count == count.max())]
    return modes


pd_data = pd.read_csv('./day-6/cereal.csv')
fiber_data = pd_data['calories']

print(fiber_data)
fiber_data = fiber_data.to_numpy()

fiber_data = np.array([0, 0, 43, 43, 43, 21,21,21])
pd_data_for_write = pd.DataFrame()

dict_of_num_arrays = {}
dict_of_out_data = {}

for i in pd_data:
    if pd_data[i].dtype == 'int64' or pd_data[i].dtype == 'float64':
        dict_of_num_arrays[i] = (pd_data[i].to_numpy())
        
        for name, arr in dict_of_num_arrays.items():
            mean = arr.mean()
            median  = np.median(arr)
            mode = get_mode(arr)
            range = f"{arr.min()}, {arr.max()}"

            sats_dict = {'mean': mean, 'median': median, 'mode': mode, 'range': range}

            dict_of_out_data[i] = sats_dict
print(dict_of_num_arrays) 
pd_data_for_write = pd.DataFrame(sats_dict)
pd_data_for_write.to_csv('./day-6/out.csv')
