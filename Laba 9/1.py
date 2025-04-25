import numpy as np
     
matrix = np.loadtxt('matrix.txt', delimiter=',')
print(np.sum(matrix), np.max(matrix), np.min(matrix))
