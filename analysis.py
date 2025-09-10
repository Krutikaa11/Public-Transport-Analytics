# --- IMPORTS ---
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- LOAD DATA ---
data = pd.read_csv("cleaned_data.csv")  # must come first

# --- BASIC ANALYSIS ---
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

# --- VISUALIZATIONS ---
# Convert date_time to datetime type
if 'date_time' in data.columns:
    data['date_time'] = pd.to_datetime(data['date_time'])

# Top 10 traffic volumes
if 'traffic_volume' in data.columns and 'date_time' in data.columns:
    top_10_traffic = data.nlargest(10, 'traffic_volume')
    plt.figure(figsize=(10,6))
    sns.barplot(x='date_time', y='traffic_volume', data=top_10_traffic, palette='viridis')
    plt.xticks(rotation=45)
    plt.title('Top 10 Traffic Volume Time Periods')
    plt.tight_layout()
    plt.savefig('top_10_traffic.png')
    plt.close()

# Traffic volume vs temperature
if 'traffic_volume' in data.columns and 'temperature' in data.columns:
    plt.figure(figsize=(10,6))
    sns.scatterplot(x='temperature', y='traffic_volume', hue='weather_type', data=data)
    plt.title('Traffic Volume vs Temperature')
    plt.tight_layout()
    plt.savefig('traffic_vs_temp.png')
    plt.close()

print("✅ Visualizations saved: top_10_traffic.png, traffic_vs_temp.png")
