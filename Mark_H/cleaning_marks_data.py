import pandas as pd

# Load Mark’s original file
df = pd.read_csv("bronx.csv")

# Rename columns to match the team format
df = df.rename(columns={
    "Date": "date",
    "City": "city",
    "Max Wind Speed (mph)": "max_wind_spd",
    "Precipitation (inch)": "precip",
    "Max Temp((°C)": "max_temp",
    "Min Temp((°C)": "min_temp"
})

# Fix the date format to YYYY-MM-DD
df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

# Reorder columns to match your team's structure
df = df[["date", "city", "max_wind_spd", "precip", "max_temp", "min_temp"]]

# Save cleaned version
df.to_csv("renamed_params_bronx.csv", index=False)

print("[SUCCESS] Cleaned file saved as 'renamed_params_bronx.csv'")