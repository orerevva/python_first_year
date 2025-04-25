import numpy as np

arr = np.random.randn(10,4)
first_5 = arr[:5]
print(arr)
print("---------------------------------------")
print(arr.min(), arr.max(), arr.mean(), arr.std())
print("---------------------------------------")
print(first_5)