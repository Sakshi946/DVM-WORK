import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Category": ["A", "B", "C", "D"],
    "Values": [10, 20, 15, 25]
}

df = pd.DataFrame(data)

print(df.describe())

plt.bar(df["Category"], df["Values"])
plt.title("Bar Chart")
plt.xlabel("Category")
plt.ylabel("Values")

plt.show()