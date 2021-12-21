import numpy as np


def matmul(x, w):
    return np.dot(x, w)

w = np.random.random((2, 2))
x = np.random.random((2, 1)).T

print(matmul(x, w))

