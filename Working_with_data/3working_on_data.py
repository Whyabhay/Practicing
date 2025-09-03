import pandas as pd

#Read CSV and first 10 rows
df = pd.read_csv("sales_data.csv")
print("WAP1: First 10 rows")
print(df.head(10))

#Number of missing values per column
print("\n: Missing values per column")
print(df.isnull().sum())

#Total and average sales
print("\n: Total and Average Sales")
print("Total Sales:", df["Sales"].sum())
print("Average Sales:", df["Sales"].mean())

#Group sales by category
print("\n: Total Sales by Category")
print(df.groupby("Category")["Sales"].sum())

#Customer who spent maximum
customer_sales = df.groupby("Customer")["Sales"].sum()
top_customer = customer_sales.idxmax()
print("\n: Top Customer")
print("Customer:", top_customer)
print("Total Spending:", customer_sales[top_customer])

#Top 5 most sold products (by category)
print("\n: Top 5 Categories by Sales")
print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False).head(5))

#Remove duplicate rows
print("\n: Duplicate rows removal")
print("Before:", len(df))
df_no_dup = df.drop_duplicates()
print("After:", len(df_no_dup))

#Correlation between numerical columns
num = df.select_dtypes("number")
print("\n: Correlation")
print(num.corr())


