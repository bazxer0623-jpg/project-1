import pandas as pd
stock1 = pd.Series([120, 80, None , 60, 95, None , 110])

stock2 = pd.Series([120, 80, None , 60, 95, None , 110],index=["Apple", "Banana", "Orange", "Mango", "Grape", "Peach", "Melon"])

stock3=stock2.to_dict()

print(stock1)
print("\n")
print(stock2)
print("\n")
print(stock3)
print("\n")

print(f"Banana庫存:{stock3['Banana']}")
print("\n")

print(stock2.isnull())
print("\n")

print(f"缺失值數量：{stock2.isnull().sum()}")
