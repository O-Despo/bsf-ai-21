import numpy as np
import matplotlib.pyplot as plt

x_train = np.linspace(-1,1,101)

while True:
    x, y = list(input("enter x then z: ").split(','))
    y_train = int(x) * x_train + np.random.randn(*x_train.shape) * float(y)
    plt.scatter(x_train, y_train)
    plt.show()


