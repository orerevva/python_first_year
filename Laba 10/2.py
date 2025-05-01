import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 1000)
ratios = [(3, 2), (3, 4), (5, 4), (5, 6)]
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
fig.suptitle('Фигуры Лиссажу с разными соотношениями частот', fontsize=14)

for ax, (fx, fy) in zip(axes.flat, ratios):
    x = np.sin(fx * t)
    y = np.sin(fy * t)
    
    ax.plot(x, y, color='blue', linewidth=1.5)
    ax.set_title(f'Соотношение частот {fx}:{fy}', fontsize=12)
    ax.grid(True)
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_aspect('equal')  

plt.tight_layout()
plt.show()