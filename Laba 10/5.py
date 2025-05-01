import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import ScalarFormatter

fig = plt.figure(figsize=(14, 6))

ax1 = fig.add_subplot(121, projection='3d')
ax1.set_title('MSE в обычном масштабе')

ax2 = fig.add_subplot(122, projection='3d')
ax2.set_title('MSE в логарифмическом масштабе (ось Z)')

w_true = 2.5  
b_true = 1.0 
w = np.linspace(0, 5, 100) 
b = np.linspace(-2, 4, 100) 
W, B = np.meshgrid(w, b)

np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = w_true * X + b_true + np.random.randn(100, 1) * 0.5

def compute_mse(W, B, X, y):
    mse = np.zeros_like(W)
    for i in range(X.shape[0]):
        y_pred = W * X[i] + B
        mse += (y_pred - y[i])**2
    return mse / X.shape[0]

MSE = compute_mse(W, B, X, y)

surf1 = ax1.plot_surface(W, B, MSE, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False, alpha=0.7)
ax1.set_xlabel('Параметр w')
ax1.set_ylabel('Параметр b')
ax1.set_zlabel('MSE')
fig.colorbar(surf1, ax=ax1, shrink=0.5, aspect=5)

MSE_log = np.log10(MSE + 1e-10)

surf2 = ax2.plot_surface(W, B, MSE_log, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False, alpha=0.7)
ax2.set_xlabel('Параметр w')
ax2.set_ylabel('Параметр b')
ax2.set_zlabel('log10(MSE)')

ax2.zaxis.set_major_formatter(ScalarFormatter())
ax2.zaxis.set_minor_formatter(ScalarFormatter())
fig.colorbar(surf2, ax=ax2, shrink=0.5, aspect=5)

plt.tight_layout()
plt.show()