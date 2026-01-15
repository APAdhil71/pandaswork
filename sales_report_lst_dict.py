import pandas as pd
sales_report = [
    {"date": "2026-01-01", "product": "Laptop", "category": "Electronics", "quantity": 2, "price": 55000, "salesperson": "Anil"},
    {"date": "2026-01-01", "product": "Mouse", "category": "Electronics", "quantity": 5, "price": 500, "salesperson": "Meera"},
    {"date": "2026-01-02", "product": "Chair", "category": "Furniture", "quantity": None, "price": 3500, "salesperson": "Rahul"},
    {"date": "2026-01-02", "product": "Desk", "category": "Furniture", "quantity": 1, "price": None, "salesperson": "Rahul"},
    {"date": "2026-01-03", "product": "Pen", "category": "Stationery", "quantity": 20, "price": 10, "salesperson": None},
    {"date": "2026-01-03", "product": "Notebook", "category": "Stationery", "quantity": 10, "price": 50, "salesperson": "Anil"},
    {"date": None, "product": "Printer", "category": "Electronics", "quantity": 1, "price": 12000, "salesperson": "Meera"},
    {"date": "2026-01-04", "product": "Monitor", "category": "Electronics", "quantity": 2, "price": None, "salesperson": "Anil"},
    {"date": "2026-01-05", "product": None, "category": "Furniture", "quantity": 1, "price": 8000, "salesperson": "Rahul"},
    {"date": "2026-01-05", "product": "Table Lamp", "category": None, "quantity": 3, "price": 1500, "salesperson": "Meera"}
]
df=pd.DataFrame(sales_report)
print(df.shape)
print(df.columns)
print(df.head())
print(df.tail())
print("info")
print(df.isnull().sum())
most_frequent_date=df["date"].mode()[0]
df["date"].fillna(most_frequent_date,inplace=True)
print(df)
df["product"].fillna("unknown", inplace=True)
print(df)
most_frequent_category=df["category"].mode()[0]
df["category"].fillna(most_frequent_category,inplace=True)
print(df)
df["quantity"].fillna(df["quantity"].mean(),inplace=True)
print(df)
df["price"].fillna(df["price"].mean(),inplace=True)
print(df)
df["salesperson"].fillna(df["salesperson"].mode()[0],inplace=True)
print(df.isnull().sum())
# sales category count
print(df["category"].value_counts())
# sales count by salesperson
print(df["salesperson"].value_counts())
# category electronics and quantity >2
print(df[(df["category"]=="Electronics") & (df["quantity"]>2)])
print(df.groupby("category")["price"].sum())
print(df.groupby("category")["quantity"].sum())
print(df.sort_values(by="price",ascending=False))
print(df.loc[2])
print(df.iloc[1])
print(df.iloc[df["price"].idxmax()])
print(df.iloc[df["price"].idxmin()])