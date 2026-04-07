import pandas as pd
import matplotlib.pyplot as plt


data = {
    "Name": ["A", "B", "C", "D"],
    "Age": [20, 21, 19, 22],
    "Marks": [80, 75, 90, 85]
}

df = pd.DataFrame(data)


print("Data Types:\n", df.dtypes)


print("\nSummary:\n", df.describe())


plt.scatter(df["Age"], df["Marks"])
plt.title("Marks vs Age")
plt.xlabel("Age")
plt.ylabel("Marks")

plt.show()