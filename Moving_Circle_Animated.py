import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
circle = plt.Circle((0, 0), 0.5)
ax.add_patch(circle)

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

def update(frame):
    circle.center = (frame, 5)
    return circle,

ani = animation.FuncAnimation(fig, update, frames=100, interval=50)
plt.show()