import pandas as pd

# Load cleaned dataset
data = pd.read_csv("cleaned_data.csv")

# Dataset info
print("✅ Dataset Info:")
print(data.info())
print("\n✅ First 5 rows:")
print(data.head())

# Top 10 busiest stations
if 'Station Name' in data.columns:
    print("\n✅ Top 10 busiest stations:")
    print(data['Station Name'].value_counts().head(10))

# Average entry count
if 'Entry Count' in data.columns:
    print("\n✅ Average Entry Count:")
    print(data['Entry Count'].mean())
