# C2 The Mathematical Building Blocks of neural Networks

## 2.1 A first look at a neural network

- We use build a MNIST model with Keras - The basic building block is a layer which extracts representations from input data
- *data distillation*: each layer gives a more meaningful representation
- *dense layer*: a layer that takes in all the input data before it (*full connected*)
- *softmax*: A layer which gives the possible outcomes as 10 probabilities adding to 1
- *compilation step*: where you chose you loss, optimizer, and metrics
- *loss function*: how the network measures its performance
- *optimizer*: the mechanism that allows the network to update itself
- *metrics*: the metrics we want to know about the model
- We also want to often reshape and scale the input data in this case form 255 to 1 on RGB values
- we then call `fit` which run the *training loop* a given amount of epochs
- we call `.evalute` to test our model

## 2.2 Data Representations for neural networks

- A *tensor* is a multi dimensional matrix
- A *tensor* is the default data for DL and ML
- A *tensor* is a container for data

### 2.2.1 - 2.2.4 Types of tensors

1. **Scalar**: a one dimensional tensor
2. **Vector**: a tensor with one axis (A vector with n entries is a n-dimensional vector)
3. **Matrices**: a 2D tensor
4. **3D and up**: and Tensor defined by its space

### 2.2.5 Key attributes

1. **Number of axes** (rank): 3D tensor had 3 axes, it can be found with `ndim`
2. **shape**: how many dimension the tensor has along each axes tuple; 3D: (2, 4, 5), 2D: (3,4), 1D: (2,), 0D: ()
3. **Data type**: the is the type of data stored in the Tensor i.e. `float64`. It can be retrieved as `dtype`

### 2.2.6 Manipulating Tensors in Numpy

- **Tensor slicing**: using the `tensor[i]` format to retrieve Tensor infomation
- You can select between any two indices

```py
tensor = shape(100, 28, 28)
tensor[10:100] // (90, 28 28)
tensor[10:100, : , : ] // (90, 28 28)
tensor[10:100, 0:28 , 0:28 ] // (90, 28 28)
tensor[: , 14: , 14: ] // (90, 28 28)
tensor[: , -14: , -14: ] // (90, 28 28)
```
### 2.2.7 Data batches

- Most of the time the first axis of a Tensor is the *batch axis* or *samples axis*
- **batch axis** (batch dimension): the axis 0
- Models dont process all the data at once they break it into batches

```py
//mnist batches of 128
batch  = tensor[:128]
batch  = tensor[128:256]
batch  = tensor[182 * n:128 * (n + 1)]
```

### 2.2.8 Real-wold examples

- Vector data: (samples, features)
- Time series data: (samples, time steps, features)
- Images: (samples, height, width channels)
- video: (samples, frames, height, width, channels)

### 2.2.9 Vector data

- A vector dataset with samples is 2D
- we have (zip, age) to predict income: (samples, features): feature = (zip, age)

### 2.2.10 Timeseries or sequence data

- If time matters use 3D
- Stock data, every minute, over year (250, 390, 3)

### 2.2.11 Image data

- There are two conventions *channels-last* and *channels-first*: Google uses (samples, height, width, color_depth)

### 2.2.12 Video data

- Video data: stored in 5D tensor

## 2.3 Gears of Neural Networks: tensor operations

- Neural Nets can be reduced to *tensor operations*
- add and multiplying tensors being examples
- A dense layer is `output = relu(dot(W, input) + b)`: where W is 2D tensor and b is a vector

### 2.3.1 Element-wise operations

- relu and addition are *element-wise* operations
- Operations that are applied independently to each entry in the tenor
- These are ideal for parallel implementations 
- we can use a for loop to make naive relu same for addition
- We will instead use Numpy functions and BLAS which are optimized
- BLAS is low lever parallel C
- Numpy is faster

### 2.3.2 Broadcasting

1. First **Broadcast axes** are added to the tensor and to match the shape of the other
2. The first tensor is repeated over the broadcast axes

- Broadcasting is needed when we add two tensors of differing shapes together
- The repetition operation is entirely virtual

### 2.3.3 Tensor Dot


