import pandas as pd
import matplotlib.pyplot as plt

# Create dataset
data = {
    "Name": ["A", "B", "C", "D"],
    "Age": [20, 21, 19, 22],
    "Marks": [80, 75, 90, 85]
}

df = pd.DataFrame(data)

# Show variable types
print("Data Types:\n", df.dtypes)

# Basic info
print("\nSummary:\n", df.describe())

# Plot (Marks vs Age)
plt.scatter(df["Age"], df["Marks"])
plt.title("Marks vs Age")
plt.xlabel("Age")
plt.ylabel("Marks")

plt.show()