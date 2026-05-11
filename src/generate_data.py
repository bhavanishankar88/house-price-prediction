import pandas as pd
import numpy as np
import os

# Set random seed
np.random.seed(42)

num_houses = 800

# Generate features
area_sqft = np.random.uniform(800, 4000, num_houses)
bedrooms = np.random.randint(1, 6, num_houses)
bathrooms = np.random.randint(1, 5, num_houses)
age_years = np.random.uniform(0, 40, num_houses)
location_tier = np.random.randint(1, 4, num_houses)

# Calculate Price in Lakhs
price = (
    15 + 
    (area_sqft * 0.035) + 
    (bedrooms * 8) + 
    (bathrooms * 6) + 
    (location_tier * 25) - 
    (age_years * 0.8)
)

# Add realistic noise
noise = np.random.normal(0, 15, num_houses)
price = price + noise

# Create DataFrame
df = pd.DataFrame({
    'area_sqft': area_sqft.round(2),
    'bedrooms': bedrooms,
    'bathrooms': bathrooms,
    'age_years': age_years.round(1),
    'location_tier': location_tier,
    'price_in_lakhs': price.round(2)
})

# Create folder and save
os.makedirs('data', exist_ok=True)
df.to_csv('data/house_data.csv', index=False)

# Final Output
print("✅ House Price Dataset Created Successfully!")
print(f"Total Houses: {len(df)}")
print(f"Average Price: ₹{df['price_in_lakhs'].mean():.2f} Lakhs")
print(f"Minimum Price: ₹{df['price_in_lakhs'].min():.2f} Lakhs")
print(f"Maximum Price: ₹{df['price_in_lakhs'].max():.2f} Lakhs")
print("\nFirst 5 rows:")
print(df.head())
print("\nColumns:", df.columns.tolist())