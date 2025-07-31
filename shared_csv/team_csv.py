# import pandas as pd

# # File paths stored in a dictionary for column checking
# csv_files = {
#     "Andrea": "../Andrea_C/final_cleaned_weather_data_selmer.csv",
#     "Brett": "../Brett_C/cleaned_weather_data_atlanta.csv",
#     "Mark": "../Mark_H/renamed_params_bronx.csv",
#     "Luis": "../Luis_V/cleaned_weather_data_oxnard.csv",
#     "Sarina": "../Sarina_P/final_cleaned_weather_data_clearwater.csv",
#     'Merhanda': "../Merhanda_P/final_cleaned_weather_data_queens.csv"
   
# }

# # 🧪 Step 1: Print column headers for all files
# print("🔎 Checking columns for each CSV:\n")
# for name, path in csv_files.items():
#     df = pd.read_csv(path)
#     print(f"{name}'s columns: {df.columns.tolist()}")

# # ✅ Step 2: Read and merge the files
# df_list = [pd.read_csv(path) for path in csv_files.values()]
# merged_df = pd.concat(df_list, ignore_index=True)

# # 💾 Step 3: Save the final team file
# merged_df.to_csv("team_weather_data.csv", index=False)
# print("\n✅ Merged CSV regenerated as team_weather_data.csv")


import pandas as pd

print("\n🔁 Building FINAL team file with Sarina's fixed Celsius data...\n")

# File paths
csv_files = {
    "Andrea": "../Andrea_C/final_cleaned_weather_data_selmer.csv",
    "Brett": "../Brett_C/cleaned_weather_data_atlanta.csv",
    "Mark": "../Mark_H/renamed_params_bronx.csv",
    "Luis": "../Luis_V/cleaned_weather_data_oxnard.csv",
    "Merhanda": "../Merhanda_P/final_cleaned_weather_data_queens.csv",
    "Sarina": "../Sarina_P/fixed_clearwater_data.csv" 
   
}

# Load and print row counts
dfs = []
for name, path in csv_files.items():
    df = pd.read_csv(path)
    print(f"✅ Loaded: {name} ({len(df)} rows)")
    dfs.append(df)

# Merge
team_df = pd.concat(dfs, ignore_index=True)
team_df.to_csv("team_weather_data.csv", index=False)

print(f"\n✅ Final team_weather_data.csv created with {len(team_df)} total rows")
