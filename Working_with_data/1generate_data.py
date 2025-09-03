import pandas as pd
import random

customers = ["Ron","Ashley","Rohit","Abhay","Sarah","Marshall"]
categories = ["Electronics", "Clothing", "Furniture", "Groceries"]

df = pd.DataFrame({ "Customer": [random.choice(customers) for _ in range(100)],
    "Category": [random.choice(categories) for _ in range(100)],
    "Sales": [random.randint(100, 5000) for _ in range(100)]})

df.to_csv("sales_data.csv", index=False)
print("sales_data.csv generated")
