# Tensor Flow API explanation

There are two aproaches to making TF models

1. `tf.keras.Sequential`: Simple and easy to use
2. The functional api: more in depth and flexible

We will mostly use the sequential API but this is worth noting.

## Ex 1

**how to make model with func api**

1. with `keras.Input()` create a input layer
2. with `keras.Dense()` (or any other layer) create a output layer
3. to stack layers use `layer3 = layer1(layer2)`
4. Use `kerad.Model()` to create the models

SN: `keras.utils.plot_model()`

### Common ground

- Training and evaluation is mostly the same between methods
- Saving works the same
- callable

### Functional API advantage

- You can reuse layers (Ex2)
- Very complex topologies
- Sharing layers
- Extract and reuse nodes in the graph of layers
- Custom layers (Ex3)

#### Functional API strengths

- Less verbose
- Model validation is done during model creation
- You can manipulate and change portions of the model

#### Functional API disadvantage

- Layers must be **DAGS** meaning recurient neural nets are not possible

#### Ex2

```python
encoder_input = keras.Input(shape=(28, 28, 1), name="img")
x = layers.Conv2D(16, 3, activation="relu")(encoder_input)
x = layers.Conv2D(32, 3, activation="relu")(x)
x = layers.MaxPooling2D(3)(x)
x = layers.Conv2D(32, 3, activation="relu")(x)
x = layers.Conv2D(16, 3, activation="relu")(x)
encoder_output = layers.GlobalMaxPooling2D()(x)

encoder = keras.Model(encoder_input, encoder_output, name="encoder")
encoder.summary()

x = layers.Reshape((4, 4, 1))(encoder_output)
x = layers.Conv2DTranspose(16, 3, activation="relu")(x)
x = layers.Conv2DTranspose(32, 3, activation="relu")(x)
x = layers.UpSampling2D(3)(x)
x = layers.Conv2DTranspose(16, 3, activation="relu")(x)
decoder_output = layers.Conv2DTranspose(1, 3, activation="relu")(x)

autoencoder = keras.Model(encoder_input, decoder_output, name="autoencoder")
autoencoder.summary()
```

```python
ass CustomDense(layers.Layer):
    def __init__(self, units=32):
            super(CustomDense, self).__init__()
                    self.units = units

                        def build(self, input_shape):
                                self.w = self.add_weight(
                                            shape=(input_shape[-1], self.units),
                                                        initializer="random_normal",
                                                                    trainable=True,
                                                                            )
                                                                                    self.b = self.add_weight(
                                                                                                shape=(self.units,), initializer="random_normal", trainable=True
                                                                                                        )

                                                                                                            def call(self, inputs):
                                                                                                                    return tf.matmul(inputs, self.w) + self.b


                                                                                                                    inputs = keras.Input((4,))
                                                                                                                    outputs = CustomDense(10)(inputs)

                                                                                                                    model = keras.Model(inputs, outputs)

```
