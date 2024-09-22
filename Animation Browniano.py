import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
num_steps = 1000  # Number of steps
time_interval = 0.01  # Time interval

# Generating random displacements
displacements = np.random.normal(0, np.sqrt(time_interval), num_steps)
positions = np.cumsum(displacements)

# Animation setup
fig, ax = plt.subplots()
line, = plt.plot([], [], lw=2)
ax.set_xlim(0, num_steps)
ax.set_ylim(np.min(positions), np.max(positions))
ax.set_title("Animação do Movimento Browniano")  # Animation title in Portuguese

def init():
    line.set_data([], [])
    return line,

def animate(i):
    x = np.arange(i)
    y = positions[:i]
    line.set_data(x, y)
    return line,

# Creating the animation
ani = FuncAnimation(fig, animate, frames=num_steps, init_func=init, blit=True)
plt.show()
