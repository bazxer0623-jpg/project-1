import pandas as pd
data = {
    "Product": ["Apple", "Banana", "Orange", "Mango", "Grape", "Guava"],
    "Price": [30, 20, 25, 60, 45, 35],
    "Sales": [100, 150, 80, 60, 90, 54]
}

df1 = pd.DataFrame(data)

print(df1.head())
print(df1.tail())

data2 = [
    ["Apple", 30, 100],
    ["Banana", 20, 150],
    ["Orange", 25, 80],
    ["Mango", 60, 60],
    ["Grape", 45, 90],
    ["Guava", 35, 54]
]

df2 = pd.DataFrame(data2, columns=["Product", "Price", "Sales"])

print(df2)

print(df2.shape)

print(df2.columns)

print(df2.dtypes)

print(df2.count())

stats = df2.describe().round(2)

print(stats)

stats.to_csv("0520_stock2.csv")