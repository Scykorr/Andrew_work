# https://coderoad.ru/53508331/%D0%9F%D1%80%D0%BE%D1%81%D1%82%D0%BE%D0%B9-%D0%B0%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC-k-%D1%81%D1%80%D0%B5%D0%B4%D0%BD%D0%B8%D1%85-%D0%B2-Python

import numpy as np
import matplotlib.pyplot as plt

DIM = 2
N = 2000
num_cluster = 11
iterations = 3

x = np.random.randn(N, DIM)
y = np.zeros(N)
# initialize clusters by picking num_cluster random points
# could improve on this by deliberately choosing most different points
for t in range(iterations):
    if t == 0:
        index_ = np.random.choice(range(N),num_cluster,replace=False)
        mean = x[index_]
    else:
        for k in range(num_cluster):
            mean[k] = np.mean(x[y==k], axis=0)
    for i in range(N):
        dist = np.sum((mean - x[i])**2, axis=1)
        pred = np.argmin(dist)
        y[i] = pred

for k in range(num_cluster):
    fig = plt.scatter(x[y==k,0], x[y==k,1])
plt.show()