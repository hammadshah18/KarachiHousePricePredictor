import streamlit as st
import joblib
import pandas as pd
import numpy as np
from pathlib import Path
import base64
# Set up the page config
st.set_page_config(page_title="🏠 Karachi House Price Predictor", layout="centered")

# Set custom background image
def set_background(image_file):
    with open(image_file, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Apply background
set_background("bg.jpg")
# Load model and data
@st.cache_resource
def load_model_and_data():
    model_path = Path(__file__).parent / "model" / "LinearRegressionModel.pkl"
    model = joblib.load(model_path)
    
    df = pd.read_csv("KarachiHouseCleanData.csv")
    return model, df

model, df = load_model_and_data()

# Get unique locations from data
locations = sorted(df["location"].unique())

# Streamlit UI
st.set_page_config(page_title="🏠 Karachi House Price Predictor", layout="centered")
st.title("🏠 Karachi House Price Predictor")
st.markdown("Predict house prices in Karachi based on location, size, and rooms.")

# User input form
with st.form("input_form"):
    location = st.selectbox("📍 Select Location", locations)
    total_sqft = st.number_input("📐 Total Area (sqft)", min_value=200.0, max_value=10000.0, step=50.0)
    bath = st.slider("🛁 Number of Bathrooms", 1, 10, step=1)
    bhk = st.slider("🛏️ Number of Bedrooms (BHK)", 1, 10, step=1)
    
    submitted = st.form_submit_button("Predict Price")

if submitted:
    # Create input DataFrame in the expected format
    X_input = pd.DataFrame([{
        "location": location,
        "total_sqft": total_sqft,
        "bath": bath,
        "bhk": bhk
    }])

    # Predict
    predicted_price = model.predict(X_input)[0]

    # Display
    if  predicted_price < 0:
        st.success(f"💰 Estimated Price: **PKR {predicted_price*-1:.2f} lakhs**")
    else:    
        st.success(f"💰 Estimated Price: **PKR {predicted_price:.2f} lakhs**")

