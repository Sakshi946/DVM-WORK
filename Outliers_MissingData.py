import pandas as pd
import numpy as np

# Dataset with missing values & outlier
data = [10, 20, 30, None, 40, 1000]

df = pd.DataFrame(data, columns=["Values"])

# Check missing values
print("Missing values:\n", df.isnull())

# Fill missing with mean
df["Values"].fillna(df["Values"].mean(), inplace=True)

# Detect outliers using IQR
Q1 = df["Values"].quantile(0.25)
Q3 = df["Values"].quantile(0.75)
IQR = Q3 - Q1

outliers = df[(df["Values"] < Q1 - 1.5*IQR) | (df["Values"] > Q3 + 1.5*IQR)]

print("\nOutliers:\n", outliers)