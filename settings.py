import streamlit as st

st.title("⚙  Settings")

st.subheader("🎨 Appearance")

if "theme" not in st.session_state:
    st.session_state.theme = "Dark"

theme = st.radio(
    "Choose Theme",
    ["Dark", "Light"],
    index=0 if st.session_state.theme == "Dark" else 1
)

st.session_state.theme = theme

st.success(f"✅ {theme} Mode Enabled")

st.subheader("🌍 Default City")

city = st.selectbox(
    "Choose Default City",
    [
        "Ahmedabad",
        "Delhi",
        "Mumbai",
        "Chennai",
        "Bengaluru",
        "Hyderabad",
        "Bhopal"
    ]
)

st.subheader("🔄 Auto Refresh")

refresh = st.selectbox(
    "Refresh Interval",
    [
        "5 Seconds",
        "10 Seconds",
        "30 Seconds"
    ]
)

st.subheader("📊 Dashboard Options")

st.checkbox("Show AQI Trend", value=True)
st.checkbox("Show Pollutant Comparison", value=True)
st.checkbox("Show Analytics", value=True)
st.checkbox("Show History", value=True)

st.subheader("🔔 Notifications")

st.toggle("AQI Alerts", value=True)
st.toggle("Daily Reminder", value=False)

st.markdown("---")

st.success("Settings saved successfully ✅")

st.markdown(
"""
### ℹ️ Project Information

**Version:** 1.0

**Machine Learning Model:** Random Forest Regressor

**Framework:** Streamlit

**Developed By:** Shreya Baranwal
"""
)