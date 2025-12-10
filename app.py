import streamlit as st
import pandas as pd
import numpy as np
import sklearn
import joblib

# ==========================
# PAGE CONFIG
# ==========================
st.set_page_config(
    page_title="Medical Disease Predictor",
    page_icon="🩺",
    layout="wide"
)

# ==========================
# HEADER
# ==========================
st.title("🩺 Medical Disease Prediction")
st.write("Masukkan data pasien untuk melakukan prediksi penyakit.")

st.markdown("---")

# ==========================
# INPUT FORM (UI ONLY)
# ==========================
with st.container():
    st.subheader("📋 Form Input Data Pasien")
    st.write("Silahkan isi variabel berikut:")

    # gunakan 2 kolom
    col1, col2 = st.columns(2)

    with col1:
        age = st.slider("Age (tahun)", 18, 90, 30)
        gender = st.selectbox("Gender", [0, 1], format_func=lambda x: "Perempuan" if x == 0 else "Laki-laki")
        weight = st.slider("Weight (kg)", 40, 150, 60)
        height = st.slider("Height (m)", 1.40, 2.00, 1.65)
        heart_rate = st.slider("Heart Rate (bpm)", 40, 149, 70)

    with col2:
        oxygen = st.slider("Oxygen Saturation (%)", 70, 100, 98)
        temperature = st.slider("Temperature (°C)", 35.0, 40.0, 36.5)
        ecg_qt = st.slider("ECG QT Interval (ms)", 300, 500, 400)
        ecg_st = st.slider("ECG ST Segment", -2.0, 2.0, 0.0)

    st.markdown("---")

    # Load the trained machine learning model
    model = joblib.load("ab.pkl")  # Load your model file

    # Prepare input data as a DataFrame
    input_data = pd.DataFrame({
        'age': [age],
        'gender': [gender],
        'weight': [weight],
        'height': [height],
        'heart_rate': [heart_rate],
        'oxygen': [oxygen],
        'temperature': [temperature],
        'ecg_qt': [ecg_qt],
        'ecg_st': [ecg_st]
    })

    # If you have preprocessing steps (like scaling), apply them
    # For example, if your model needs standard scaling:
    # scaler = joblib.load("/mnt/data/scaler.pkl")  # If you've saved a scaler model
    # input_data_scaled = scaler.transform(input_data)  # Apply scaling

    # Predict button action
    if st.button("🔍 Predict"):
        # Make prediction
        prediction = model.predict(input_data)
        
        # Display prediction result
        st.write(f"Predicted Disease: {prediction[0]}")

# ==========================
# FOOTER
# ==========================
st.markdown("---")
st.caption("UI version — Model diterapkan dan siap digunakan.")


