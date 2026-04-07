import matplotlib.pyplot as plt


categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

x = [1, 2, 3, 4]
y = [5, 15, 10, 20]


plt.figure(figsize=(10, 5))


plt.subplot(1, 2, 1)
plt.bar(categories, values)
plt.title("Bar Graph")


plt.subplot(1, 2, 2)
plt.scatter(x, y)
plt.title("Scatter Plot")

plt.tight_layout()
plt.show()