# Numpy

Numpy is a library for working with linear algebra and matrices in python. Python's lists are slow Numpys are way fast (50x). It is widely used for scientific computing and used a lot in tensor flow.

## You have to install and import NP

Run `pip3 install numpy` to install. Use `import numpy as np` to add numpy to a python script. It is a norm that we use `np` as a alias for numpy.

## Array Creations

As you know matrices are MxN dimensional collections of numbers in math terms. In coding terms they are pretty much the same thing.

| 3, 4, 2 |
| 1, 2, 1 |

If you were to code it up with python and numpy respectively.

```py
arr = [[3, 4, 2], [1, 3, 1]]
arr = np.array([
        [3, 4, 2],
        [1, 3, 1]
        ])
```
- NP arrays are indexed the same as math matrices (row, col), but use the format `A[row, col]` instead of $A_{row,col}$

- **array**: fixed size container of items with same type and size
- dims defined by shape
- **axes**: what NP call dimensions
- **vector**: array with a single dimension
- **matrix**: array with 2 dimensions 
- **tensor**: for 3D or higher

## The attributes of a array

- `ndarray.ndim`: tells you the number of axes or dimensions
- `ndarray.size`: total number of elements
- `ndarray.shape`: returns a tuple of ints each integer representing the number of elements on that axis
- `ndarray.dtype`: the data type of elements in a array
- `ndarray.itemsize`: the byte size of each element of the array
- `ndarray.data`: buffer with array elements. Not usually needed because we use indexing

## Basic array operations

- When a element wise operation is done a new array is created and filled with results
- **element wise**: each element of the output array is a combination of the input arrays equivalent elements.
- `+ - / *` all work as expected
- `+=` and its derivatives also work
- There are many useful methods `ndarray.sum()`: this is known as a universal function
- 
## Why numpy and what the difference with python

- All elements in NP array are homogeneous
- Because NP only has all the same type in arrays it can do optimized operations
- NP array faster and more compact the Python list.
- NP uses less memory
- NP allows to specify data type

## NP basics

- **ndarray**: shorthand for n-dimensional array, array with any number of dimensions. It is also the main class for NP arrays.

## Indexing

ex. 

```python
a = np.arange(10)**3

#a= array([  0,   1,   8,  27,  64, 125, 216, 343, 512, 729])

a[2]
8

a[2:5]
array([ 8, 27, 64])

# equivalent to a[0:6:2] = 1000;

# from start to position 6, exclusive, set every 2nd element to 1000

a[:6:2] = 1000

a
array([1000,    1, 1000,   27, 1000,  125,  216,  343,  512,  729])

a[::-1]  # reversed a
array([ 729,  512,  343,  216,  125, 1000,   27, 1000,    1, 1000])
```

- `ndarray.flat()` delvers each elm as if on 1D array

## Shape manipulation

- **Shape**: a tuple of the number of elements on each axis
- Following commands return new version and do not modify original array
- `ndarray.ravel()`: return flattened array
- `ndarray.reshape()`: returns array w/ modified shape (Dose not change original)
- `ndarray.resize()`: same as reshape but changes original
- `ndarray.T`: returns array transposed

## Stacking different arrays

- `np.hstack()`: stacks alon second axis
- `np.vstack()`: stacks along first acis
- `np.concatenate()`: has a optional arg for axis of concat
- `r_` and `c_` can be user as literals for stacking `np.r_[1:4, 0, 4] => array([1, 2, 3, 0, 4])`

## Spliting a array into smaller ones

- `np.vsplit()`: split along vertical axis
- `np.hsplit()`: along horizontal axis
- `np.array_split()`: along specified axis

## Copies and views

- No copy at all: a variable just points to another array
- View or shallow: Share the same data and not shape
  - check with `ndarray.flags.owndata`
  - Base `ndarray.base` is the original array
  - slicing a array returns a view
- Deep Copy: `ndarray.copy()` fully copies data to new `ndarray`


## Copies and views

- No copy at all: a variable just points to another array
- View or shallow: Share the same data and not shape
  - check with `ndarray.flags.owndata`
  - Base `ndarray.base` is the original array
  - slicing a array returns a view
- Deep Copy: `ndarray.copy()` fully copies data to new `ndarray`

## Broadcasting Rules

1. If two array do not have same shape '1's dims will be added to the smaller
2. size 1 in a axis is repeatedly to the maximum of the largest matrix

