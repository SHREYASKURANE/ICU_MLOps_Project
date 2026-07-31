import streamlit as st
import pandas as pd
import joblib
import os

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="ICU Patient Survival Prediction",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 ICU Patient Survival Prediction")
st.write("Predict whether an ICU patient is likely to survive based on clinical parameters.")

# -----------------------------
# Load Model
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "models", "best_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "models", "scaler.pkl")

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# -----------------------------
# User Inputs
# -----------------------------
st.header("Enter Patient Information")

age = st.number_input("Age", min_value=0, max_value=120, value=40)

age_group = st.number_input("Age Group", min_value=0, max_value=10, value=2)

sex = st.selectbox(
    "Sex",
    [0, 1],
    format_func=lambda x: "Male" if x == 1 else "Female"
)

infection = st.selectbox(
    "Infection Present",
    [0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

sysbp = st.number_input(
    "Systolic Blood Pressure",
    min_value=50,
    max_value=250,
    value=120
)

pulse = st.number_input(
    "Pulse Rate",
    min_value=20,
    max_value=220,
    value=80
)

emergency = st.selectbox(
    "Emergency Admission",
    [0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict"):

    input_data = pd.DataFrame(
        [[
            age,
            age_group,
            sex,
            infection,
            sysbp,
            pulse,
            emergency
        ]],
        columns=[
            "Age",
            "AgeGroup",
            "Sex",
            "Infection",
            "SysBP",
            "Pulse",
            "Emergency"
        ]
    )

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.success("✅ Prediction: Patient is likely to Survive")
    else:
        st.error("❌ Prediction: Patient is unlikely to Survive")