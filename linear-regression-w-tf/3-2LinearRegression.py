import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers 

import numpy as np
import matplotlib.pyplot as plt

learn_rate = 0.01
epochs = 100

x = 2
y = .3

x_train = np.linspace(-1,1,1000)
y_train = int(x) * x_train + np.random.randn(*x_train.shape) * float(y)

plt.scatter(x_train, y_train)
plt.show()

model = keras.Sequential(
    [
    layers.Dense(1)
    ])

y_predict = model.predict([[3]])
model.summary()

print(y_predict)

model.compile(optimizer=tf.optimizers.Adam(learning_rate=0.1), loss="mean_absolute_error", metrics=['accuracy'], loss_weights=None,
              sample_weight_mode=None, weighted_metrics=None)


model.fit(x_train, y_train, epochs=100)

val = model.layers[0].kernel
print(val)

y_predict = model.predict([[1],[-2],[45]])
print(y_predict)