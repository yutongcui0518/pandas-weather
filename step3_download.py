import pandas as pd

URL = "https://corgis-edu.github.io/corgis/datasets/csv/weather/weather.csv"

df = pd.read_csv(URL)

df.to_csv("weather_local_copy.csv", index=False)

print("Rows, Cols =", df.shape)
print("Saved -> weather_local_copy.csv")
