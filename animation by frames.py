import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Initial settings
fig, ax = plt.subplots()
ax.set_xlim(0, 10)  # Set the limits of the x-axis
ax.set_ylim(0, 10)  # Set the limits of the y-axis

# Create an initial star
star_points = np.array([[5, 6], [5.5, 4], [7, 4], [5.8, 3], [6.2, 1],
                        [5, 2], [3.8, 1], [4.2, 3], [3, 4], [4.5, 4]])
star = plt.Polygon(star_points, closed=True, color='black')
ax.add_patch(star)

def update(frame):
    # Rotate the star
    angle = frame * 0.1
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    rotated_star_points = np.dot(star_points - [5, 5], rotation_matrix) + [5, 5]
    star.set_xy(rotated_star_points)
    return star,

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), repeat=True)

# Display the animation
plt.show()
