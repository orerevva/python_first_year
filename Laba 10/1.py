import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

fig, ax = plt.subplots(figsize=(10, 6))
x = np.linspace(-1, 1, 400)
degrees = range(1, 8)
colors = plt.cm.rainbow(np.linspace(0, 1, len(degrees)))

for n, color in zip(degrees, colors):
    Pn = legendre(n)
    y = Pn(x)
    line, = ax.plot(x, y, color=color, label=f'n = {n}')
    x_annot = 0.8 
    y_annot = Pn(x_annot)
    offset_y = (n - 4) * 0.1  
    
    ax.annotate(f'n = {n}', 
                xy=(x_annot, y_annot),
                xytext=(10, offset_y * 100), 
                textcoords='offset points',
                color=color,
                va='center')

ax.set_title('Полиномы Лежандра', fontsize=14)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('P_n(x)', fontsize=12)
ax.grid(True)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1.1)

plt.tight_layout()
plt.show()