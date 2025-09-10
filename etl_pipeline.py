import pandas as pd

# Load the real Indian Metro dataset
data = pd.read_csv("indian_metro_data.csv")

# Drop missing values
data = data.dropna()

# Save cleaned data
data.to_csv("cleaned_data.csv", index=False)

print("✅ ETL pipeline completed. Cleaned data saved as cleaned_data.csv")
