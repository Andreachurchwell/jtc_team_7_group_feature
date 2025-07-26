import requests
import pandas as pd
from datetime import datetime, timedelta
import time
import os

# === SETTINGS ===
API_KEY = "2ff07141d53f4644ae9976067779d00e"
CITY = "Clearwater"
STATE = "FL"
COUNTRY = "US"
UNITS = "I"  # Imperial (Fahrenheit, inches, mph)
FOLDER = "Sarina_P"
RAW_FILE = f"{FOLDER}/raw_weather_data_clearwater.csv"
FINAL_FILE = f"{FOLDER}/final_cleaned_weather_data_clearwater.csv"

# Create folder if not exists
os.makedirs(FOLDER, exist_ok=True)

# === STEP 1: DOWNLOAD HISTORICAL WEATHER DATA ===
print("📡 Starting Weatherbit download...")

start_date = datetime(2023, 7, 25)
end_date = datetime(2024, 7, 25)
base_url = "https://api.weatherbit.io/v2.0/history/daily"
records = []

current = start_date
while current < end_date:
    chunk_start = current
    chunk_end = min(current + timedelta(days=29), end_date)

    print(f"[FETCHING] {chunk_start.date()} to {chunk_end.date()}")

    params = {
        "city": CITY,
        "state": STATE,
        "country": COUNTRY,
        "start_date": chunk_start.strftime("%Y-%m-%d"),
        "end_date": chunk_end.strftime("%Y-%m-%d"),
        "key": API_KEY,
        "units": UNITS
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()["data"]

        for day in data:
            records.append({
                "date": day["datetime"],
                "city": f"{CITY}, {STATE}",
                "min_temp": day["min_temp"],
                "max_temp": day["max_temp"],
                "precip": day["precip"],
                "max_wind_spd": day["max_wind_spd"]
            })

    except Exception as e:
        print(f"[ERROR] Failed to fetch {chunk_start.date()} to {chunk_end.date()}: {e}")

    current += timedelta(days=30)
    time.sleep(1)  # Prevent rate-limit issues

# Save raw file
df = pd.DataFrame(records)
df.to_csv(RAW_FILE, index=False)
print(f"\n✅ Raw data saved to {RAW_FILE}")

# === STEP 2: CLEAN THE DATA ===
print("\n🧼 Cleaning data...")

# Fill missing values
df["precip"] = df["precip"].fillna(0)
df["max_temp"] = df["max_temp"].fillna(df["max_temp"].mean())
df["min_temp"] = df["min_temp"].fillna(df["min_temp"].mean())
df["max_wind_spd"] = df["max_wind_spd"].fillna(df["max_wind_spd"].mean())

# Drop duplicate rows
before = len(df)
df = df.drop_duplicates()
after = len(df)
print(f"[INFO] Removed {before - after} duplicate rows")

# Format date and sort
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Final output
df.to_csv(FINAL_FILE, index=False)
print(f"\n🎉 Final cleaned data saved to {FINAL_FILE}")
