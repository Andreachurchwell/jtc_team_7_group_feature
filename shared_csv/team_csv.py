import pandas as pd


# List of cleaned CSVs with proper folder paths
csv_files = [
    "../Andrea_C/final_cleaned_weather_data_selmer.csv",
    "../Brett_C/cleaned_weather_data_atlanta.csv",
    "../Mark_H/renamed_params_bronx.csv",
    "../Luis_V/cleaned_weather_data_oxnard.csv"
]

# Load and concatenate
df_list = [pd.read_csv(file) for file in csv_files]
merged_df = pd.concat(df_list, ignore_index=True)

# Save merged version
merged_df.to_csv("team_weather_data.csv", index=False)
print("Merged CSV saved as team_weather_data.csv")
