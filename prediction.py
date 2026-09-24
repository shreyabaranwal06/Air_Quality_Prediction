import streamlit as st
import pandas as pd
import joblib

# ==========================
# Load Model
# ==========================

model = joblib.load("model/aqi_model.pkl")

st.title("🤖 AI Air Quality Prediction")

st.write("Enter pollutant values to predict AQI")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    pm25 = st.number_input("PM2.5", min_value=0.0, max_value=500.0, value=30.0)
    pm10 = st.number_input("PM10", min_value=0.0, max_value=600.0, value=60.0)
    no2 = st.number_input("NO₂", min_value=0.0, max_value=300.0, value=20.0)

with col2:
    so2 = st.number_input("SO₂", min_value=0.0, max_value=300.0, value=10.0)
    co = st.number_input("CO", min_value=0.0, max_value=20.0, value=1.0)
    o3 = st.number_input("O₃", min_value=0.0, max_value=300.0, value=25.0)

st.markdown("---")

if st.button("🔮 Predict AQI", width="stretch"):

    input_df = pd.DataFrame({
        "PM2.5": [pm25],
        "PM10": [pm10],
        "NO2": [no2],
        "SO2": [so2],
        "CO": [co],
        "O3": [o3]
    })

    prediction = model.predict(input_df)[0]

    st.success(f"✅ Predicted AQI : {prediction:.2f}")

    if prediction <= 50:
        st.success("🟢 Category : Good")
        st.info("Air quality is good. Outdoor activities are safe.")

    elif prediction <= 100:
        st.info("🟡 Category : Satisfactory")
        st.info("Air quality is acceptable for most people.")

    elif prediction <= 200:
        st.warning("🟠 Category : Moderate")
        st.warning("Sensitive people should reduce prolonged outdoor activity.")

    elif prediction <= 300:
        st.error("🔴 Category : Poor")
        st.error("Avoid long outdoor exposure.")

    else:
        st.error("🟣 Category : Very Poor")
        st.error("Stay indoors whenever possible.")
