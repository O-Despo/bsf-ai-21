""" Fastion_Mnist_basics:
    A basic implemneation of Fastion MNIST
"""
from tensorflow.keras import datasets, layers, Sequential, losses
#import numpy as np
#import matplotlib.pyplot as plt

#Load the dataset
fashion_mnist = datasets.fashion_mnist
(train_imgs, train_labels), (test_imgs, test_labels) = fashion_mnist.load_data()

class_names = ['t-shirt', 'pants', 'hoodie', 'dress', 'coat',
               'sandal', 'shirt', 'sneaker', 'bag', 'ankle boot']

#Nomalize data
train_imgs = train_imgs / 255.0
test_imgs = test_imgs / 255.0

model = Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(10)
    ])

model.compile(optimizer='adam', loss=losses.SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy'])
model.fit(train_imgs, train_labels, epochs=15)
loss, acc = model.evaluate(test_imgs, test_labels)
print(f"loss:{loss}, acc:{acc}")
