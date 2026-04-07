import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y = [10, 25, 30, 45, 50]

plt.plot(x, y, marker='o')
plt.title("X-Y Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid()

plt.show()