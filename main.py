import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("regression_model.joblib")

# App title
st.title("Package Prediction App")

st.write("Enter your CGPA to predict the expected package.")

# User input
cgpa = st.number_input(
    "CGPA",
    min_value=0.0,
    max_value=10.0,
    step=0.01
)

# Predict button
if st.button("Predict Package"):
    input_data = np.array([[cgpa]])

    prediction = model.predict(input_data)

    package = float(prediction.flatten()[0])

    st.success(f"Predicted Package: {package:.2f} LPA")