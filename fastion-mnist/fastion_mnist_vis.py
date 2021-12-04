""" Fastion_Mnist_basics:
    A basic implemneation of Fastion MNIST
"""
from tensorflow.keras import datasets, layers, Sequential, losses
#import numpy as np
import matplotlib.pyplot as plt


#Load the dataset
fashion_mnist = datasets.fashion_mnist
(train_imgs, train_labels), (test_imgs, test_labels) = fashion_mnist.load_data()

plt.figure()
plt.imshow(train_imgs[0])
plt.show()

#Nomalize data
train_imgs = train_imgs / 255.0
test_imgs = test_imgs / 255.0

plt.figure()
plt.imshow(train_imgs[0])
plt.show()
