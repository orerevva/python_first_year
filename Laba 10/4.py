import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig = plt.figure(figsize=(12, 8))
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.25, top=0.9, hspace=0.5)

ax1 = plt.subplot(3, 1, 1)
wave1, = ax1.plot([], [], lw=2, color='pink')
ax1.set_title('Волна 1: A1*sin(ω1*x)')
ax1.set_xlim(0, 4*np.pi)
ax1.set_ylim(-2, 2)
ax1.grid(True)

ax2 = plt.subplot(3, 1, 2)
wave2, = ax2.plot([], [], lw=2, color='purple')
ax2.set_title('Волна 2: A2*sin(ω2*x)')
ax2.set_xlim(0, 4*np.pi)
ax2.set_ylim(-2, 2)
ax2.grid(True)

ax3 = plt.subplot(3, 1, 3)
result, = ax3.plot([], [], lw=2, color='red')
ax3.set_title('Результат сложения: A1*sin(ω1*x) + A2*sin(ω2*x)')
ax3.set_xlim(0, 4*np.pi)
ax3.set_ylim(-4, 4)
ax3.grid(True)

axcolor = 'lightgoldenrodyellow'

ax_A1 = plt.axes([0.2, 0.15, 0.65, 0.03], facecolor=axcolor)
ax_omega1 = plt.axes([0.2, 0.10, 0.65, 0.03], facecolor=axcolor)

A1_slider = Slider(ax_A1, 'Амплитуда 1 (A1)', 0.1, 2.0, valinit=1.0)
omega1_slider = Slider(ax_omega1, 'Частота 1 (ω1)', 0.1, 2.0, valinit=1.0)

ax_A2 = plt.axes([0.2, 0.05, 0.65, 0.03], facecolor=axcolor)
ax_omega2 = plt.axes([0.2, 0.00, 0.65, 0.03], facecolor=axcolor)

A2_slider = Slider(ax_A2, 'Амплитуда 2 (A2)', 0.1, 2.0, valinit=1.0)
omega2_slider = Slider(ax_omega2, 'Частота 2 (ω2)', 0.1, 2.0, valinit=1.0)

x = np.linspace(0, 4*np.pi, 1000)

def update(val):
    A1 = A1_slider.val
    omega1 = omega1_slider.val
    A2 = A2_slider.val
    omega2 = omega2_slider.val
    
    y1 = A1 * np.sin(omega1 * x)
    y2 = A2 * np.sin(omega2 * x)
    y_result = y1 + y2
    
    wave1.set_data(x, y1)
    wave2.set_data(x, y2)
    result.set_data(x, y_result)
    
    ax1.set_ylim(-A1*1.1, A1*1.1)
    ax2.set_ylim(-A2*1.1, A2*1.1)
    ax3.set_ylim(-(A1+A2)*1.1, (A1+A2)*1.1)
    
    fig.canvas.draw_idle()

A1_slider.on_changed(update)
omega1_slider.on_changed(update)
A2_slider.on_changed(update)
omega2_slider.on_changed(update)

update(None)

plt.show()