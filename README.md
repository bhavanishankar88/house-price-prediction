# 🏠 House Price Prediction - Machine Learning Web App

A Machine Learning web application that predicts house prices based on area, bedrooms, bathrooms, age, and location.

## ✨ Features
- Real-time house price prediction
- User-friendly web interface using Streamlit
- Trained using Linear Regression model
- Clean and professional design

## 🛠 Technologies Used
- **Python**
- **Scikit-learn** (Machine Learning)
- **Streamlit** (Web App)
- **Pandas & NumPy**
- **Joblib** (Model Saving)

## 📊 Model Details
- **Algorithm**: Linear Regression
- **Dataset**: Synthetic realistic housing data (800 samples)
- **Features**: Area (sqft), Bedrooms, Bathrooms, Age, Location Tier
- **Target**: Price in Lakhs

## 🚀 How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/bhavanishankar88/house-price-prediction.git

# 2. Go inside the project
cd house-price-prediction

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run streamlit_app.py