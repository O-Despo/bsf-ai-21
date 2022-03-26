# Notes for 22-03-26

## Main ideas

- *Pandas* is a Python library that makes working with many file type easy
- *Pandas* is closely integrated with *Numpy*
- *Pandas* introduces two new data types
  - *series* a 1D array which acts as the columns of a table
  - *DataFrame* a object that represents the whole table and contains *series* within it
- Unicode is a standard for encoding text for more details check out [Universal Coded Character Set](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set), [Unicode website](https://home.unicode.org/basic-info/overview/), or [the Unicode Consortium](https://en.wikipedia.org/wiki/Unicode_Consortium)
- CSV (Comma separated values) is a file formate that store tables using only commas and newlines. It is commonly used in code for its simplicity
- The data type of a *ndarray* array is defined by the most complex element of the array

e.g.

```py
arr = np.array([3, 4, 2, 43.34])
print(arr.dtype)
```

In the example above the dtype would be `float64` even though most of the elements are `int64` because the most complex data type is `float64` therefor to store all the elements *Numpy* uses `float64`. Note the `ndarray`s will always have only one data type. This is not true for pure Python arrays.

- A *ndarray* cannot be appended to and only has one data type it can store
- The *np.loadtext()* function is used to load CSV files in *ndarray* but it the normal data type rules apply
- Among many advantages Pandas *DataFrames* allow for any of its supported data types to be loaded and used without having the entire *DataFrame* be the same data type. Only *Series* must be the same data type.
- *DataFrames* help must be indexed differently then *ndarrays*. Mainly using built in functions.
- Using Pandas we can easly do complete many statistics tasks that we have gone over in the past.

## Notes from after session

- C is a low level language made in 1972 by Denis Ritchie
- C was very impactful for many reasons including in portability
- I HIGHLY recommend this video on why C was so impactful [C Video](https://www.youtube.com/watch?v=ci1PJexnfNE) (This also touches on why Linux based on Unix is so good at dealing with multiple users)
- C++ is like a improved version of C with new features and support for OOP(Object oriented programming)
- C# is also closely derived from C
- Python (and many other language) have things that were first done in C
- Rust is another lang you might find interesting it is very fast for how nice it is to code in (or so I have heard)
- That C book I recommend is commonly called K&R and pretty much legendary at this point

## Extra links

- [Rust](https://www.rust-lang.org/)
- [Pandas](https://pandas.pydata.org/)
- [Numpy](https://numpy.org/)