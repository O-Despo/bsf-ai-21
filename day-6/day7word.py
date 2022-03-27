import numpy as np
import math

arr = np.array([0, 4, 3, 2, 4, 3, 2, 1, 2])

#Mean (average)
#The Mode (the number the most in a list)

#Median (one in the middle)
# print(len(arr))

len_d2 = len(arr)/2
if len(arr)%2 == 0:
    median = (arr[int(len_d2)] + arr[int(len_d2+1)]) /2
else:
    median = arr[int(len_d2)]

print(median)
#Range (min and max)
# print([arr.min(), arr.max()])