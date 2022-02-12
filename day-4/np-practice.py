from pydoc import visiblename
import numpy as np

print(np.__version__)
print(np.show_config())
print(np.info(np.add))

# np.all and all
# x = np.array([
#     [3, 4],
#     [0, 1]
# ])

# print(x.all())

# x = np.array([
#     [0, 0],
#     [0, 0]
# ])

# Types
# s = np.array([
#     [1, 3, 232],
#     [4, 'hello', 12]
# ])

# i = np.array([
#     [1, 3, 232],
#     [3, 1.0, 1]
# ])

# z = np.array([
#     [4, 23, 12],
#     [3, 2, 1]
# ])

# print(s.dtype)
# print(i.dtype)
# print(z.dtype)

# print(type(s[0][1]))
# print(type(i[0][1]))
# print(type(z[0][1]))

# print("t" + s[0][2])

# Array shapes

z = np.array([
    [4, 23, 12],
    [3, 2, 1]
])

print(z.ndim)
print(z.shape)
print(z.shape)

# Methods of making arrays

array = np.array([4, 5, 2])
all_zeros = np.zeros([4, 2])
all_ones = np.zeros([5, 2])
all_empty = np.empty([3, 3])
range_arr = np.arange(5, 50, 2)

print(all_zeros)

# Reshapeing

b = np.ones([3, 2])

print(b)

b = b.reshape((2, 3))

print(b)

b = b.reshape([1, 6])

print(b)

b = b.reshape([-1, 2])

print(b)

# Adding axes to arrays

b = b[np.newaxis, :]
print(b)

# Indexing and slicing

b = np.arange(0, 300, 3).reshape([10, -1])

print(b[4])
print(b[4:7, 3])
print(b[-6, 3])

# Index by condition

print(b > 5)
print(b[b%2 == 0])

# Creating arrays from existing arrays 

b = np.arange(0, 40, 2).reshape([4, -1])

a = b[1]
a[2] = 93

print(b)

# Reverse and transpose

b.T
print(b)

b= np.flip(b, axis=0)
print(b)

b = b.flatten()
print(b)

# Operations

b = np.arange(0, 624, 39).reshape(8, -1)

print(b)

print(b/3.2)
print(b + 54)

b = np.arange(0, 21).reshape(7, 3)
a = np.arange(0, 63, 3).reshape(3, 7)

print(np.dot(b, a))

b = np.arange(-40, 40).reshape(5, 16)
print(np.abs(b))

# Applying functions

def sigmoid(x):
    return 1 / (1 + np.exp(x))

print(sigmoid(b))