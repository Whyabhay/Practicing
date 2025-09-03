Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
==== RESTART: C:/Users/Win-10/Desktop/Projects/Practicing/working_on_data.py ===
WAP1: First 10 rows
   Customer     Category  Sales
0     Abhay  Electronics   4282
1       Ron  Electronics   1167
2     Abhay    Groceries    395
3     Sarah    Groceries    888
4     Sarah    Furniture   1973
5    Ashley    Furniture   1713
6  Marshall  Electronics   1178
7  Marshall  Electronics   2366
8     Sarah  Electronics   3744
9  Marshall  Electronics    485

: Missing values per column
Customer    0
Category    0
Sales       0
dtype: int64

: Total and Average Sales
Total Sales: 247617
Average Sales: 2476.17

: Total Sales by Category
Category
Clothing       79935
Electronics    72012
Furniture      52849
Groceries      42821
Name: Sales, dtype: int64

: Top Customer
Customer: Rohit
Total Spending: 52580

: Top 5 Categories by Sales
Category
Clothing       79935
Electronics    72012
Furniture      52849
Groceries      42821
Name: Sales, dtype: int64

: Duplicate rows removal
Before: 100
After: 100

: Correlation
       Sales
Sales    1.0
