import pandas as pd
df = pd.read_csv("weather_local_copy.csv")

# 1) 所有州（看有没有 PA/NJ）
print("States:", sorted(df["Station.State"].dropna().unique().tolist()))

# 2) 直接搜城市名里包含 'phil'
print("\nCities containing 'phil':")
print(
    df[df["Station.City"].str.contains("phil", case=False, na=False)]
      [["Station.City", "Station.State", "Station.Code"]]
      .drop_duplicates()
      .head(50)
)

# 3) 看看 PA 州里有哪些城市/代码
print("\nStations in PA:")
print(
    df[df["Station.State"] == "PA"]
      [["Station.City", "Station.Code"]]
      .drop_duplicates()
      .sort_values("Station.City")
      .head(100)
)

# 4) 看看 NJ 州里有哪些（有时费城对应的 WFO 在新泽西 Mount Holly）
print("\nStations in NJ:")
print(
    df[df["Station.State"] == "NJ"]
      [["Station.City", "Station.Code"]]
      .drop_duplicates()
      .sort_values("Station.City")
      .head(100)
)

# 5) 直接查 WFO 代码是否有 "PHI"
print("\nRows with Station.Code == 'PHI':")
print(
    df[df["Station.Code"].astype(str).str.upper().eq("PHI")]
      [["Station.City", "Station.State", "Station.Code"]]
      .head(20)
)
