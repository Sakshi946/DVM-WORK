import matplotlib.pyplot as plt

fig, ax = plt.subplots()
circle = plt.Circle((5, 5), 0.5)
ax.add_patch(circle)

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

def on_key(event):
    x, y = circle.center

    if event.key == 'up':
        circle.center = (x, y + 0.5)
    elif event.key == 'down':
        circle.center = (x, y - 0.5)
    elif event.key == 'left':
        circle.center = (x - 0.5, y)
    elif event.key == 'right':
        circle.center = (x + 0.5, y)

    fig.canvas.draw()

fig.canvas.mpl_connect('key_press_event', on_key)

plt.title("Use Arrow Keys to Move Circle")
plt.show()