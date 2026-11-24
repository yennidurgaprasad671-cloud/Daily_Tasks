"""1. Sales Threshold Filtering
You are given monthly sales:
sales = np.array([12000, 18000, 9000, 22000, 15000, 30000])
Task:
● Filter all sales values greater than the average sales
● Return the filtered array."""
import numpy as np

sales = np.array([12000, 18000, 9000, 22000, 15000, 30000])
filtered_sales = sales[sales > np.mean(sales)]
print(filtered_sales)
