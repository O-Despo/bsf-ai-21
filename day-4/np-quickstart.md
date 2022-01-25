# NumPy Quickstart

## Objectives

1. understand understand n-dim arrays
2. understand how to apply linear operations
3. understand properties of n-dim arrays

## The Basics

- base class called `ndarray`
- dimensions are called *axes*
  
### `ndarray` properties

- `.ndim`: the axis(dims) of the array
- `.shape`: the dimension of the array in the forms of a tuple of the size of each dimension
- `.size`: the total number of elements in the array
- `.dtype`: the data type of elements in a array
- `.itemsize`: the byte size of each element of the array
- `.data`: buffer with array elements. Not usually needed because we use indexing

## Array creation

1. passing normal python array to `np.array(input_arr, dtype=)`
   1. A `dtype` can be explicitly passed
2. You can also make arrays with placeholder content
3. Growing array = expensive operation
4. `np.zeros(shape)`: creates zeros array
5. `np.ones(shape)`: array of ones
6. `np.empty(shape)`: uses whatever is already in memory
7. `np.arange(start, end_not_incuded, step)`: makes a range
8. `np.linespace(start, end_not_in, step)`: used when making a range for floats

## Printing arrays

- the last axis is printed from left to right,
- the second-to-last is printed from top to bottom,
- the rest are also printed from top to bottom, with each slice separated from the next by an empty line.
- numpy skips the central parts of large arrays. This can be changes with `np.set_printoptions(threshold=sys.maxsize)`
  

## Basic operations

- When a element wise operation is done a new array is created and filled with results
- `*` operates element wise
- operations like `+=` and `*=` server to modify the current array
- **upcasting**: when two arrays operated on together one being a diffrent `dtype` the most precise data type is used 
- unary operations implements as methods of `ndarray`, i.e. `ndarray.sum()`
- specifying a axis for unary operations dose that operation along the given axis
  
## Universal functions

- A function like `sin` is implemented as a "universal function" `ufunc`: operate element wise
- ex.  `np.sqrt(B)`

## Indexing, Slicing and iterating

- 1D arrays like py arrays

ex. 

```python
a = np.arange(10)**3

a
array([  0,   1,   8,  27,  64, 125, 216, 343, 512, 729])

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

- Multidim arrays can have one index per axis `(axis, axis)`

```python
def f(x, y):

    return 10 * x + y


b = np.fromfunction(f, (5, 4), dtype=int)

b
array([[ 0,  1,  2,  3],
       [10, 11, 12, 13],
       [20, 21, 22, 23],
       [30, 31, 32, 33],
       [40, 41, 42, 43]])

b[2, 3]
23

b[0:5, 1]  # each row in the second column of b
array([ 1, 11, 21, 31, 41])

b[:, 1]    # equivalent to the previous example
array([ 1, 11, 21, 31, 41])

b[1:3, :]  # each column in the second and third row of b
array([[10, 11, 12, 13],
```

- If a axes is missing a complete slice is implied
- You can also write every other acis be full axes with ... ex `b[i, ...]`
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

## Functions and methods

Look at them in source

## Broadcasting Rules

1. If two array do not have same shape '1's dims will be added to the smaller
2. size 1 in a axis is repeatedly to the maximum of the largest matrix