import numpy as np
import math

arr = np.array([1, 4, 12, 18, 19, 40, 50])

arr_len = len(arr) / 2
if len(arr)%2 != 0:
    med = arr[int(arr_len/2)]
else:
    med = arr[math.floor(arr_len/2) + round(arr_len/2)]

print(len(arr.shape))

print(med)
