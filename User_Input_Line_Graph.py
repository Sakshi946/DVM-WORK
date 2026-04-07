import matplotlib.pyplot as plt

try:
    n = int(input("Enter number of points: "))
except ValueError:
    print(" Please enter a valid number!")
    exit()

x = []
y = []

for i in range(n):
    xi = int(input(f"Enter x[{i}]: "))
    yi = int(input(f"Enter y[{i}]: "))
    x.append(xi)
    y.append(yi)

plt.plot(x, y, marker='o')
plt.title("Line Graph")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid()
plt.show()