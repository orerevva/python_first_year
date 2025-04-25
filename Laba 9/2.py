import numpy as np 

x = np.array([2, 2, 2, 3, 3, 3, 5])
ch = np.where(x[:-1] != x[1:])[0] + 1
index = np.concatenate(([0], ch, [len(x)]))
vl = x[index[:-1]]
counts = np.diff(index)
print(vl, counts)