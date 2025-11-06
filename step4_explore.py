import pandas as pd

df = pd.read_csv("weather_local_copy.csv")  # 先不解析日期，看看原始列
print("=== head(5) ===")
print(df.head())

print("\n=== shape ===")
print(df.shape)

print("\n=== columns ===")
print(df.columns.tolist())

print("\n=== dtypes ===")
print(df.dtypes)
