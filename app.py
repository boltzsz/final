import streamlit as st

# ==========================
#  PAGE CONFIG
# ==========================
st.set_page_config(
    page_title="Medical Disease Predictor",
    page_icon="🩺",
    layout="wide"
)

# ==========================
#  HEADER
# ==========================
st.title("🩺 Medical Disease Prediction")
st.write("Masukkan data pasien untuk melakukan prediksi penyakit. (UI Only)")

st.markdown("---")

# ==========================
#  INPUT FORM (UI ONLY)
# ==========================
with st.container():
    st.subheader("📋 Form Input Data Pasien")
    st.write("Silahkan isi variabel berikut:")

    # gunakan 2 kolom
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age (tahun)", min_value=18, max_value=90, value=30, step=1)
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

    # Tombol UI saja (belum ada fungsi prediksi)
    st.button("🔍 Predict", help="Tombol ini belum terhubung ke model.")

# ==========================
#  FOOTER
# ==========================
st.markdown("---")
st.caption("UI version — Model belum diterapkan")


