import matplotlib.pyplot as plt

data = [10, 20, 20, 30, 30, 30, 40, 40, 50, 60]

plt.hist(data)

plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")

plt.grid()

plt.show()