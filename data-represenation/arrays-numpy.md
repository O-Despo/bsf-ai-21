# Numpy

## Slicing

```py
img_dataset[10:50, :, :]
img_dataset[10:50]

img_dataset.shape()
```

**sample axis**: The first axis in datasets is usasly the smaple.

## Batching

You often want to group our databases as we do not have enough ram to store the data. This is called batching.

```py
batch_1 = img_dataset[:125]
batch_2 = img_dataset[125:250]
`````
