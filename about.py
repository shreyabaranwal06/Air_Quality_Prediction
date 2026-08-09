import streamlit as st

st.title("ℹ️ About this Dashboard")

st.markdown("""
<div style="
background:#14213d;
padding:25px;
border-radius:15px;
border:1px solid #1e3a5f;
">

<p style="font-size:22px;color:#4FC3F7;">
This AI Air Quality Prediction Dashboard provides:</p>


<p style="font-size:15px;">✅ Real-Time Air Quality Monitoring</p>
<p style="font-size:15px;">✅ AI-Based AQI Prediction</p>
<p style="font-size:15px;">✅ Last 7 Days AQI Trend Analysis</p>
<p style="font-size:15px;">✅ Pollutant Comparison (PM2.5, PM10, NO₂, SO₂, CO, O₃)</p>
<p style="font-size:15px;">✅ AQI Category Distribution</p>
<p style="font-size:15px;">✅ City-wise Air Quality Analysis</p>
<p style="font-size:15px;">✅ Monthly AQI Trend Visualization</p>
<p style="font-size:15px;">✅ Correlation Heatmap</p>
<p style="font-size:15px;">✅ Interactive Analytics Dashboard</p>
<p style="font-size:15px;">✅ PDF Report Generation</p>
<p style="font-size:15px;">✅ CSV Data Export</p>

<hr>

<h3 style="color:#4FC3F7;">🛠️ Technologies Used</h3>

<ul style="font-size:15px;">
<li>Python</li>
<li>Streamlit</li>
<li>Pandas</li>
<li>NumPy</li>
<li>Plotly</li>
<li>Scikit-learn</li>
<li>Joblib</li>
<li>ReportLab</li>
</ul>

<h3 style="color:#4FC3F7;">🤖 Machine Learning Model</h3>

<p style="font-size:15px;">
Random Forest Regressor is used to predict the Air Quality Index (AQI)
based on pollutant concentrations such as PM2.5, PM10, NO₂, SO₂, CO and O₃.
</p>

<h3 style="color:#4FC3F7;">🎯 Project Objective</h3>

<p style="font-size:15px;">
The objective of this project is to monitor air pollution, visualize historical
air quality data, analyze pollution trends, and provide AI-based AQI prediction
to support better environmental awareness and decision making.
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown(
"""
<center>

### 👩‍💻 Developed By

**Shreya Baranwal**

B.Tech (CSE - AI)

Python • Machine Learning • Streamlit • Data Analytics

</center>
""",
unsafe_allow_html=True
)

st.caption(
"© 2026 AI Air Quality Prediction Dashboard | Developed using Python, Streamlit & Machine Learning"
)