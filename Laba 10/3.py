import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

fig, ax = plt.subplots(figsize=(10, 10))
plt.subplots_adjust(bottom=0.2) 

line, = ax.plot([], [], lw=2)
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.grid(True)
ax.set_title('Фигура Лиссажу с изменяющимся соотношением частот.')

t = np.linspace(0, 2*np.pi, 1000)
phase_shift = 0 

ax_slider = plt.axes([0.2, 0.05, 0.6, 0.03])
freq_ratio_slider = Slider(
    ax=ax_slider,
    label='Соотношение частот (fy/fx)',
    valmin=0,
    valmax=1,
    valinit=0,
    valstep=0.01
)

def init():
    line.set_data([], [])
    return line,


def update(frame):
    freq_ratio = frame / 100 
    
    x = np.sin(t)
    y = np.sin(freq_ratio * t + phase_shift)
    
    line.set_data(x, y)
    
    ax.set_title(f'Фигура Лиссажу: fy/fx = {freq_ratio:.2f}, φ = {phase_shift}')
    
    return line,

def update_slider(val):
    freq_ratio = freq_ratio_slider.val
    
    x = np.sin(t)
    y = np.sin(freq_ratio * t + phase_shift)
    
    line.set_data(x, y)
    ax.set_title(f'Фигура Лиссажу: fy/fx = {freq_ratio:.2f}, φ = {phase_shift}')
    fig.canvas.draw_idle()

freq_ratio_slider.on_changed(update_slider)

ani = FuncAnimation(
    fig=fig,
    func=update,
    frames=np.arange(0, 101, 1),
    init_func=init,
    blit=True,
    interval=50,
    repeat=True
)

plt.show()