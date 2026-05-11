import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,r2_score
import joblib
import os

df = pd.read_csv('data/house_data.csv')

print("✅ dataset loaded successfully!")
print("shape", df.shape)

X = df[['area_sqft','bedrooms','bathrooms','age_years','location_tier']]

y = df['price_in_lakhs']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 42)

model = LinearRegression()

model.fit(X_train,y_train)

os.makedirs('models',exist_ok=True)
joblib.dump(model,'models/house_price_model.pkl')

y_pred = model.predict(X_test)

print("✅model trained and saved successfully!")
print(f"R2 score:{r2_score(y_test,y_pred):.4f}")
print(f"MAE:{mean_absolute_error(y_test,y_pred):.2f}lakhs")

coefficients = model.coef_
features = X.columns


print("\nFeature Importance:")
for feature, coef in zip(features, coefficients):
    print(f"{feature}: {coef:.4f}")