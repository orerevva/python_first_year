import numpy as np

x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0]) 
zero_index = np.where(x[:-1] == 0)[0]
next_index = x[zero_index + 1]
#if len(next_index) > 0:  
#    mx = np.max(next_index)
#else:
 #   None
print(np.max(next_index))