import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
x, y = [], []
line, = ax.plot([], [])

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

def update(frame):
    x.append(frame)
    y.append(frame)
    line.set_data(x, y)
    return line,

ani = animation.FuncAnimation(fig, update, frames=10, interval=500)
plt.show()