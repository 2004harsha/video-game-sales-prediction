import streamlit as st
import pandas as pd
import joblib


# Load saved model
model = joblib.load("xgb_model.joblib")

# Streamlit app
st.title("Video Game Global Sales Predictor")

st.markdown("Enter game details to predict Global Sales (in millions of copies):")

platform = st.selectbox("Platform", ['PS2', 'X360', 'PS3', 'Wii', 'DS', 'PS4', 'PC', '3DS', 'PS'])
genre = st.selectbox("Genre", ['Action', 'Sports', 'Shooter', 'Role-Playing', 'Platform', 'Misc', 'Racing', 'Fighting', 'Puzzle'])
publisher = st.text_input("Publisher", "Nintendo")
year = st.slider("Year", 1980, 2020, 2010)
na_sales = st.slider("NA Sales (in millions)", 0.0, 50.0, 1.0)
eu_sales = st.slider("EU Sales (in millions)", 0.0, 50.0, 1.0)
jp_sales = st.slider("JP Sales (in millions)", 0.0, 50.0, 1.0)
other_sales = st.slider("Other Sales (in millions)", 0.0, 50.0, 1.0)

# Create input DataFrame
input_df = pd.DataFrame({
    'Platform': [platform],
    'Genre': [genre],
    'Publisher': [publisher],
    'Year': [year],
    'NA_Sales': [na_sales],
    'EU_Sales': [eu_sales],
    'JP_Sales': [jp_sales],
    'Other_Sales': [other_sales]
})

if st.button("Predict Global Sales"):
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Global Sales: {prediction:.2f} million copies")
