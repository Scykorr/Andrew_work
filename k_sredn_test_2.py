import numpy as np
import matplotlib.pyplot as plt

DIM = 2
N = 100
num_cluster = 2
iterations = 3

x = np.random.randn(N, DIM)
y = np.zeros(N)

for t in range(iterations):
    if t == 0:
        index = np.random.choice(range(N), num_cluster, replace=False)
        mean = x[index]
    else:
        for k in range(num_cluster):
            mean[k] = np.mean(x[y == k], axis=0)
    for i in range(N):
        dist = np.sum((mean - x[i])**2, axis=1)
        pred = np.argmin(dist)
        y[i] = pred

for k in range(num_cluster):
    fig = plt.scatter(x[y == k, 0], x[y == k, 1])
plt.show()