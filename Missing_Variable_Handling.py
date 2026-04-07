import numpy as np

data = [10, 20, None, 40, None, 60]

# Replace None with mean
clean_data = [x for x in data if x is not None]
mean_val = sum(clean_data) / len(clean_data)

final_data = [x if x is not None else mean_val for x in data]

print("Original:", data)
print("After Handling Missing Values:", final_data)