import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y = [10, 30, 20, 50, 40]

plt.plot(x, y, marker='o')

plt.title("Line Chart")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.grid()

plt.show()