import pandas as pd
import requests

# Step 1: Fetch dataset (temporary dummy CSV from GitHub)
url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"
data = pd.read_csv(url)

# Step 2: Clean data (remove rows with missing values)
data = data.dropna()

# Step 3: Save cleaned data locally
data.to_csv("cleaned_data.csv", index=False)

print("✅ ETL pipeline completed. Cleaned data saved as cleaned_data.csv")
