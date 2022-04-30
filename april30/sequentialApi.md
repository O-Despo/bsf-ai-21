# The Sequential Model
//+source+https://www.tensorflow.org/guide/keras/sequential_model

The `Sequential model is usefull for a linear model

```python 
model = keras.Sequential(
        [
                layers.Dense(2, activation="relu", name="layer1"),
                layers.Dense(3, activation="relu", name="layer2")
                layers.Dense(2, name="output")
        ]
)

x = tf.ones((3, 3))
y = model(x)

#equiv to

layers.Dense(2, activation="relu", name="layer1"),
layers.Dense(3, activation="relu", name="layer2")
layers.Dense(2, name="output")

x = tf.ones((3,3))
y = layer3(layer2(layer1))
```

### Sequential model disadvantages
- dose not support multiple inputs / outputs
- no layers can have multiple inputs / outputs
- no layer sharing
- no non-linear topology

## Creation

- Pass layers to `keras.Sequential()`
- Or use `model.add(layer)`

\\+SN+`model.layers` and `model.pop()`

- Layers need to know the shape of the input to know the create the weights
- When you first create a layers the weights are unintalized
- Weights are made on the first call

\\+SN+`layer.weights` / `model.summary()`

- A `keras.Input()` object can be added to the model before adding other layers so the weights can be compiled
- `model.add(keras.Input(shape=(4,)))` or `model.add(layers.Dense(2, activation="relu", input_shape(4,)))`
- Best practive to define the input of a sequentail model

### Debuging workflow

- You can use `model.add()` and `model.summary()` to add to a model as it goes on
- After complilation you can extract layers from the model


