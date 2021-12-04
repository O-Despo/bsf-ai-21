# Tensors and basic data arrays

In tensorflow we store data in tensors. Tensors are n-dimenstional arrays.

## Major types of tensors

### scalar (0D)

A number.

```py
import numpy as np
x = np.array(12)
x.ndim()
```

### Vector (1D)

```py
x = np.array([12, 21, 3, 3])
x.ndim()
```

### Matricies (2D)

```py
x = np.array([[12, 23, 12],
              [2, 23, 12],
              [23, 2, 23]
              ])
x.ndim()
```

### 3d Tensors (3D)

```py
x = np.array([[
                [12, 23],
                [1, 2]],
                [[2, 4],
                [1, 2]]
        ]
```

### Key ellements

- **Rank**: number of axis
- **shape**: how many dimenstions each array has
- **data type**: the Dtype of the array

# Numpy

## Slicing

```py
img_dataset[10:50, :, :]
img_dataset[10:50]

img_dataset.shape()
```

**sample axis**: The first axis in dataset is usaly used for samples. By moving along this axis we move through the samples.

This first axis is not always the sample axis, in the case of batching it is instead called the **batch axis**

## Batching

You often want to group our databases as we do not have enough ram to store the data. This is called batching.

```py
batch_1 = img_dataset[:125]
batch_2 = img_dataset[125:250]
```

How would me make it go to the nth batch?

```py
def get_n_batch(n, batch_size = 125):
        return img_dataset[batch_size * n: batch_size + (n + 1)]
```

## Real world tensors

*Vector data*: a 2D tensor (sample, features)
*squence data*: 3D (samples, timesteps, features)
*images*: (samples, height, width, channels) (samples, channels, height, width)

e.x: if you wanted a datatset of people and number of cars they own by zip code.

This would be a vector dataset. Given 1000 people the shape would be (1000, 2)
