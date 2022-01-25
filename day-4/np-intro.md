# Numpy the absolute basics for beginners

[source-numpy](https://numpy.org/doc/stable/user/absolute_beginners.html)
[source-w3](https://www.w3schools.com/python/numpy/numpy_copy_vs_view.asp)
## Welcome to NP

- **NumPy**: Numerical Python
- Standard for working with python data
- Used in Pandas, SCiPy, MatPlotlib, scikit-learn,scikit-image
- provide **ndarray** homogenous n-dimensional array object

## install

```pip install numpy```

## import

```python
import numpy as np
```

## Diff between Python List and NumPy array

- All elements in NP array are homogeneous
- Because NP only has all the same type in arrays it can do optimized operations
- NP array faster and more compact the Python list.
- NP uses less memory
- NP allows to specify data type

## What is an  Array

- Man data structure for NP
- **Array**: grid of values contains raw data, how to locate elm, how to interpret
- `dtype`
- **Possible indexes**: a array can be indexed by tuple of non-negative ints, bools, another array, or all ints
- **Rank**: the number of dimensions of a array
- **shape**: tuple of integers giving array size along each dimension

## initialization

```python
a = np.array([1, 2, 3])
a = np.array([[1, 3, 2], [1, 2, 3]])
print(a[0])
```

Accessed elm with `[]`

## More information about arrays

- **ndarray**: shorthand for n-dimensional array, array with any number of dimensions
- `ndarray`: call used to represent matrices and vectors
- **vector**: array with a sing dimension
- **matrix**: array with 2D
- **tensor**: for 3D or higher

#### Attrs of array

- **array**: fixed size container of items with same type and size
- dims defined by shape
- **axes**: what NP call dimensions

e.i.

```
[[0., 0., 0.],
 [1., 1., 1.]]
```

- Has two axes
- arrays can be accessed and modified by indexing and slicing
- arrays can point to each other
- **attributes**: information intrinsic to the array

## How to create a basic array

1. `np.array([1, 2, 4)`
2. `np.zeros(2)` returns `array([0., 0.])`
3. `np.ones(2)` returns `array([1., 1.])`
4. `np.empty(2)` reutunr `array([ 3.14, 42.  ])  # may vary`

- **np.empty()**: creates a array with the states of the memory already in place so it is somewhat random

## Adding, removing, and sorting elements¶

- `np.sort()`: sorts elements
- `np.concatenate()`: concatenate

```python
arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
np.sort(arr)
#array([1, 2, 3, 4, 5, 6, 7, 8])

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

np.concatenate((a, b))
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
np.concatenate((x, y), axis=0)
```

### other sort options

- `argsort`: indirect sort along a specified axis, 
- `lexsort`: indirect stable sort
- `searchsort`: fined elms in arr
- `partition`: partial sort

## How to know the shape and size of a array

- `ndarray.ndim`: tell you the number of axes or dimensions
- `ndarray.size`: total number of elements
- `ndarray.shape`: returns a tuple of ints each integer representing the number of elements on that axis

```python
array_example = np.array([[[0, 1, 2, 3],

                           [4, 5, 6, 7]],


                          [[0, 1, 2, 3],

                           [4, 5, 6, 7]],


                          [[0 ,1 ,2, 3],

                           [4, 5, 6, 7]]])

array_example.ndim #(3)
array_example.size #(24)
array_example.shape #(3, 2, 4)
```

## Reshape an array

- `ndarray.reshape()`: gives the array a new shape without altering data
- `np.reshape(input, newshape, order)`: reshapes a array with more options that `ndarray.reshape()`
- when referring to `np.reshape()` the parameter `order` describes method of storage in memory C-like index order or Fortan-like index order

- A reshaped array should have the same number of elements as the original array


```python
a = np.arange(6)
print(a)

b = a.reshape(3, 2)
print(b)

np.reshape(a, newshape=(1, 6), order='C')
```

## Adding new acis to an array

- `np.newaxis()`: increases the axis of a arr by 1
- `np.expand_dims()`: add new acis in a specified positions

- **row vector**: a vector with the 1 axis along the first dimension
- **col vector**: a vector with the 1 axis along the second dimension

```python
a1 = np.arange(6)
print(a1.shape)

row_vec = a[np.newaxis, :]
print(row_vec.shape)

col_vec = a[:, np.newaxis]
print(col_vec)
```

```python
a = np.arange(6)
print(a.shape)

b = np.expand_dims(a, axis=1)
print(b.shape)
```

##  Indexing and slicing

- Slicing and indexing is similar to python lists
- `ndarray[]` allows for slicing and indexing of a array
- `np.mgrid[]`: creates a multi-dim mesh 

```python
a = np.array([1, 2, 3])
print(a[1])
print(a[0:1])
print(a[1:])
print(a[-2:])
```

### Index by condition 

```python
a = np.array([[1, 2, 3, 4],[5, 6, 7, 8], [9, 10, 11, 12]])
print(a[a<5])
divisible_by_2 = a[a%2==0]
print(divisible_by_2)

# Logical operators
five_up = (a > 5) | (a == 5)

print(five_up)
```

### Nonzero

- `np.nonzero()`: print the indcies of elements that meet a condition

```python
b = np.nonzero(a < 5)
print(b) #(array([0, 0, 0, 0]), array([0, 1, 2, 3]))
list_of_coordinates= list(zip(b[0], b[1]))
```

## Creating arrays from existing data

- You can make a array by slicing
- `np.vstack()`: stacks the input arrays vertically
- `np.hstack()`: stacks the input arrays horizontally
- `np.hsplit()`: allows to split a array to predefined shapes
- `np.hsplit(input, (col_to_split_at, col_to_split_at))`
- `np.hsplit(input, how_to_divide)`

```python
a = np.arange(10)
a1 = a[2:5]

a1 = np.array([[1, 1],

               [2, 2]])

a2 = np.array([[3, 3],

               [4, 4]])

b = np.vstack((a1, a2))
print(b)

b = np.hstack((a1, a2))
print(b)

# Hsplit

x = np.arange(1, 25).reshape(2, 12)
print(np.hsplit(x, 3))
print(np.hsplit(x, (3, 4)))
```

## Views

- When you derive a array form another is creates a `view` in Numpy. This is not new data it rather points to the old data. It is known as a *shallow copy*. If you use the `.copy()` method it creates a new array in memory a *deep copy*. 

```python
b2 = a.copy()
```

## Basic array operations

- `np.ones(number_of_elements, dtype=)`: creates all ones data
- `np.sum(axis=)`: sums the elms of a array by the axis
- You can do `*`, `/`, `+`, and `-` and they work as expected

```python
data = np.array([1, 2])
ones = np.ones(2, dtype=int)
data + ones
```
## Broadcasting

- Broadcasting allows for compatible arrays to be multiplied including scalar operations. If they are not compatible it returns a `ValueError`

```python
data = np.array([1.0, 2.0])
data * 1.6
```

## More array ops

- `ndarray.min()`
- `ndarray.max()`
- `ndarray.sim()`
- for each you can specify a axis to check 

## Creating Matrices

```python
np.ones(3)
#array([1., 1., 1.])

np.zeros(3)
#array([0., 0., 0.])

rng = np.random.default_rng()  # the simplest way to generate random numbers

rng.random(3) 
#array([0.63696169, 0.26978671, 0.04097352])

np.ones((3, 2))
#array([[1., 1.],
#       [1., 1.],
#       [1., 1.]])

np.zeros((3, 2))
#array([[0., 0.],
#       [0., 0.],
#       [0., 0.]])

rng.random((3, 2)) 
```

## Generating random numbers

- `np.random.default_rng()`: returns a object that can make random numbers
- `rng.intergers(max_num_not_included, size=)`: generates random array of integers 

## Get unique items and counts

- `np.unique()`: returns unique elements
- `np.unique(input_array, return_index=, return_counts=, axis=)`: returns unique elements or rows or column

## Transposing and reshaping

- `np.transpose()` or `ndarray.T` transposes a array

## Reverse array

- `np.flip(input, axis=)`: reveres the array

## Reshape and flatten multidimensional arrays

- `np.flatten(input)`: makes a array 1-Dim dose makes a copy 
- `np.ravel()`: same as flatten but changes parent array 
