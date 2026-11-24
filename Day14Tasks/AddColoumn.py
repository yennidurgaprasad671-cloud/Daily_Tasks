"""5. Adding and Updating Columns
A DataFrame:
df = pd.DataFrame({
"Price": [100, 200, 300]
})
Scenario:
● Add a column Discount = 10% of Price
● Add another column Final Price = Price - Discoun"""
import pandas as pd

df = pd.DataFrame({"Price": [100, 200, 300]})

# Add Discount and Final Price columns
df["Discount"] = df["Price"] * 0.10
df["Final Price"] = df["Price"] - df["Discount"]

print(df)
