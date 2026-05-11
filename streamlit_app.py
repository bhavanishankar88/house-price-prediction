import streamlit as st
import pandas as pd
import joblib

# Set page configuration - Must be the first Streamlit command
st.set_page_config(
    page_title="House Price Predictor", 
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 House Price Prediction")
st.markdown("### Predict house prices using Machine Learning")

# Load the model
@st.cache_resource
def load_model():
    return joblib.load('models/house_price_model.pkl')

model = load_model()

# Input fields
col1, col2 = st.columns(2)

with col1:
    area_sqft = st.number_input("Area (sq.ft)", min_value=500, max_value=5000, value=1500)
    bedrooms = st.selectbox("Number of Bedrooms", [1, 2, 3, 4, 5])
    bathrooms = st.selectbox("Number of Bathrooms", [1, 2, 3, 4])

with col2:
    age_years = st.number_input("Age of House (years)", min_value=0, max_value=50, value=5)
    location_tier = st.selectbox("Location Tier", 
                               [1, 2, 3],
                               format_func=lambda x: ["Prime Location", "Good Location", "Normal Area"][x-1])

# Prediction Button
if st.button("🔮 Predict House Price", type="primary"):
    input_data = pd.DataFrame({
        'area_sqft': [area_sqft],
        'bedrooms': [bedrooms],
        'bathrooms': [bathrooms],
        'age_years': [age_years],
        'location_tier': [location_tier]
    })
    
    prediction = model.predict(input_data)[0]
    
    st.success(f"**Predicted House Price: ₹ {prediction:.2f} Lakhs**")

st.caption("Built with Linear Regression • House Price Predictor")