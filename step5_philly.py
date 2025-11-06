import pandas as pd

df = pd.read_csv("weather_local_copy.csv", parse_dates=["Date.Full"])

# Add handy aliases (keep original columns intact)
df["Precip"] = df["Data.Precipitation"]
df["Temp_Avg"] = df["Data.Temperature.Avg Temp"]
df["Temp_Max"] = df["Data.Temperature.Max Temp"]
df["Temp_Min"] = df["Data.Temperature.Min Temp"]
df["Wind_Speed"] = df["Data.Wind.Speed"]
df["City"] = df["Station.City"]
df["State"] = df["Station.State"]

# 1) Filter to Philadelphia, PA
phl = df[(df["City"] == "Philadelphia") & (df["State"] == "Pennsylvania")].copy()
if phl.empty:
    raise SystemExit("No rows found for Philadelphia, PA. Check City/State values.")

# 2) Average temperature (prefer Avg; otherwise use (Max+Min)/2)
if phl["Temp_Avg"].notna().any():
    avg_temp = phl["Temp_Avg"].mean()
else:
    avg_temp = ((phl["Temp_Max"] + phl["Temp_Min"]) / 2).mean()

# 3) Hottest and coldest day
hot_row = phl.loc[phl["Temp_Max"].idxmax()]
cold_row = phl.loc[phl["Temp_Min"].idxmin()]

# 4) Total precipitation & number of rainy days (>0)
total_precip = phl["Precip"].sum()
rainy_days = int((phl["Precip"] > 0).sum())

print("=== Philadelphia, PA — Summary ===")
print(f"Average temperature: {avg_temp:.2f}")
print(f"Hottest day: {hot_row['Date.Full'].date()} | Max {hot_row['Temp_Max']}")
print(f"Coldest day: {cold_row['Date.Full'].date()} | Min {cold_row['Temp_Min']}")
print(f"Total precipitation: {total_precip:.2f}")
print(f"Rainy days (precip > 0): {rainy_days}")
