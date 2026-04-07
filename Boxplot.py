import matplotlib.pyplot as plt

data = [10, 20, 30, 40, 50, 60, 100]  # 100 is outlier

plt.boxplot(data)

plt.title("Box Plot")
plt.ylabel("Values")

plt.show()