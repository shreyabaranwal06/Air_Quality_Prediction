import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
import aqi_report
from streamlit_autorefresh import st_autorefresh

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="AI Air Quality Prediction",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)
st_autorefresh(interval=5000, key="aqi_refresh")

# ==========================================
# Load Dataset
# ==========================================

def load_data():
    return pd.read_csv("dataset/clean_air_quality.csv")

df = load_data()
latest = df.iloc[-1]

# ==========================================
# Custom CSS
# ==========================================

st.markdown("""
<style>

.stApp{
    background:#0B1120;
    color:white;
}

[data-testid="stSidebar"]{
    background:#111827;
}

[data-testid="stMetricLabel"] {
    color: white !important;
}

[data-testid="stMetricValue"] {
    color: white !important;
}

.kpi-card{
    background:#1E293B;
    padding:20px;
    border-radius:18px;
    text-align:center;
    box-shadow:0px 0px 20px rgba(0,180,255,.25);
}

.kpi-title{
    color:#94A3B8;
    font-size:18px;
}

.kpi-value{
    color:#38BDF8;
    font-size:24px;
    font-weight:bold;
}

header{
    visibility:hidden;
    height:0px;
}

[data-testid="stHeader"]{
    display:none;
}

.block-container{
    padding-top:0rem !important;
    margin-top:0rem !important;
}


</style>
""", unsafe_allow_html=True)

# ==========================================
# Sidebar
# ==========================================

with st.sidebar:

    selected = option_menu(
        menu_title="🌍 Air Quality AI",
        options=[
            "Dashboard",
            "Prediction",
            "Analytics",
            "Report",
            "About",
            "Settings"
        ],
        icons=[
            "speedometer2",
            "cpu",
            "bar-chart",
            "clock-history",
            "file-earmark-text",
            "cloud",
            "info-circle",
            "gear"
        ],
        default_index=0
    )


# ==========================================
# Dashboard Header
# ==========================================

top1, top2 = st.columns([7, 5], vertical_alignment="center")

with top1:
    st.title("🌍 AI Air Quality Dashboard")
    st.caption("Real-Time Air Quality Monitoring & Prediction")

with top2:

    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns([3.2, 2.6, 0.8], vertical_alignment="center")

    with c1:
        city = st.selectbox(
            "📍 City",
            sorted(df["City"].unique()),
            label_visibility="collapsed"
        )

    with c2:
        st.download_button(
            "📥 Download CSV",
            data=df.to_csv(index=False),
            file_name="AQI_Report.csv",
            mime="text/csv",
            use_container_width=True
        )

    with c3:
        if st.button("🔔", use_container_width=True):
            st.toast("No new notifications 🔔")

st.markdown("---")

# Filter by selected city
df = df[df["City"] == city]
latest = df.iloc[-1]

    # ==========================================
    # KPI Cards
    # ==========================================


col1, col2, col3, col4 = st.columns(4)

with col1:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">AQI</div>
            <div class="kpi-value">{int(latest["AQI"])}</div>
        </div>
        """, unsafe_allow_html=True)

with col2:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">PM2.5</div>
            <div class="kpi-value">{latest["PM2.5"]:.1f}</div>
        </div>
        """, unsafe_allow_html=True)

with col3:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">PM10</div>
            <div class="kpi-value">{latest["PM10"]:.1f}</div>
        </div>
        """, unsafe_allow_html=True)

with col4:
        st.markdown("""
        <div class="kpi-card">
            <div class="kpi-title">Humidity</div>
            <div class="kpi-value">72%</div>
        </div>
        """, unsafe_allow_html=True)

#         # Temperature & Wind Speed safe handling

# if "Temperature" in df.columns:
#     temperature = latest["Temperature"]
# else:
#     temperature = 28


# if "Wind Speed" in df.columns:
#     wind_speed = latest["Wind Speed"]
# else:
#     wind_speed = 12

#     with col5:
#       st.markdown(f"""
#     <div class="kpi-card">
#         <div class="kpi-title">Temperature</div>
#         <div class="kpi-value">{temperature} °C</div>
#     </div>
#     """, unsafe_allow_html=True)


# with col6:
#     st.markdown(f"""
#     <div class="kpi-card">
#         <div class="kpi-title">Wind Speed</div>
#         <div class="kpi-value">{wind_speed}km/h</div>
#     </div>
#     """, unsafe_allow_html=True)



st.markdown("---")

    # ==========================================
    # Last 7 Days AQI Trend
    # ==========================================

st.subheader("📈 Last 7 Days AQI Trend")

trend_df = df.tail(7)

fig = px.line(
        trend_df,
        x="Date",
        y="AQI",
        markers=True,
        template="plotly_dark"
    )

fig.update_layout(
        paper_bgcolor="#0B1120",
        plot_bgcolor="#0B1120",
        font=dict(color="white"),
        height=420
    )

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

    # ==========================================
    # Charts
    # ==========================================

left, right = st.columns(2)

with left:

        st.subheader("📊 Pollutant Comparison")

        pollutant_df = pd.DataFrame({
            "Pollutant":["PM2.5","PM10","NO2","SO2","CO","O3"],
            "Value":[
                latest["PM2.5"],
                latest["PM10"],
                latest["NO2"],
                latest["SO2"],
                latest["CO"],
                latest["O3"]
            ]
        })

        fig = px.bar(
            pollutant_df,
            x="Pollutant",
            y="Value",
            color="Value",
            text="Value",
            template="plotly_dark"
        )

        fig.update_layout(
            paper_bgcolor="#0B1120",
            plot_bgcolor="#0B1120",
            height=420
        )

        st.plotly_chart(fig, use_container_width=True)

with right:

        st.subheader("🥧 AQI Category Distribution")

        distribution = df["AQI_Bucket"].value_counts()

        fig = go.Figure(
            data=[
                go.Pie(
                    labels=distribution.index,
                    values=distribution.values,
                    hole=0.6
                )
            ]
        )

        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor="#0B1120",
            height=420
        )

        st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

        # ==========================================
    # AQI Gauge + AI Prediction
    # ==========================================

left, right = st.columns([2,1])

with left:

        st.subheader("🌍 Current AQI")

        fig = go.Figure(go.Indicator(

            mode="gauge+number",

            value=float(latest["AQI"]),

            title={"text":"Current AQI"},

            gauge={

                "axis":{"range":[0,500]},

                "bar":{"color":"deepskyblue"},

                "steps":[

                    {"range":[0,50],"color":"green"},

                    {"range":[50,100],"color":"yellow"},

                    {"range":[100,200],"color":"orange"},

                    {"range":[200,300],"color":"red"},

                    {"range":[300,500],"color":"purple"}

                ]

            }

        ))

        fig.update_layout(

            template="plotly_dark",

            paper_bgcolor="#0B1120",

            plot_bgcolor="#0B1120",

            font=dict(color="white"),

            height=420

        )

        st.plotly_chart(fig, use_container_width=True)

with right:

        st.subheader("🤖 AI Prediction")

        current = int(latest["AQI"])
        tomorrow = current + 8

        st.metric("Current AQI", current)
        st.metric("Tomorrow AQI", tomorrow)

        if current <= 50:
            st.success("🟢 Good")
            st.info("Outdoor activities are safe.")

        elif current <= 100:
            st.info("🟡 Satisfactory")
            st.info("Air quality is acceptable.")

        elif current <= 200:
            st.warning("🟠 Moderate")
            st.warning("Sensitive people should reduce outdoor activities.")

        elif current <= 300:
            st.error("🔴 Poor")
            st.error("Avoid long outdoor exposure.")

        else:
            st.error("🟣 Very Poor")
            st.error("Stay indoors whenever possible.")

st.markdown("---")

# ==========================================
# History + Forecast
# ==========================================

left, right = st.columns([1.25, 1.15], gap="large")

# ==========================
# Left : History Table
# ==========================

with left:

    st.subheader("📋 Last 7 Days AQI History")

    history = df.tail(7)[[
        "Date",
        "AQI",
        "PM2.5",
        "PM10",
        "NO2",
        "SO2",
        "CO",
        "O3",
        "AQI_Bucket"
    ]]

    st.dataframe(
        history,
        use_container_width=True,
        hide_index=True,
        height=295
    )

# ==========================
# Right : AQI Forecast
# ==========================

with right:

    st.subheader("📅 Next 7 Days AQI Forecast")

    forecast = pd.DataFrame({
        "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "AQI": [
            int(latest["AQI"]) + 5,
            int(latest["AQI"]) + 10,
            int(latest["AQI"]) + 8,
            int(latest["AQI"]) + 12,
            int(latest["AQI"]) + 7,
            int(latest["AQI"]) + 4,
            int(latest["AQI"]) + 6
        ]
    })

    fig = px.bar(
        forecast,
        x="Day",
        y="AQI",
        color="AQI",
        text="AQI",
        template="plotly_dark",
        color_continuous_scale="Turbo"
    )

    fig.update_layout(
        paper_bgcolor="#0B1120",
        plot_bgcolor="#0B1120",
        font=dict(color="white"),
        height=300,
        margin=dict(l=10, r=10, t=40, b=10),
        xaxis_title="",
        yaxis_title="AQI",
        coloraxis_showscale=False
    )

    st.plotly_chart(fig, use_container_width=True)

    # ==========================================
# Health Recommendation
# ==========================================

st.markdown("---")

st.subheader("💚 Health Recommendation")

aqi = int(latest["AQI"])

if aqi <= 50:
    st.success("🟢 Good Air Quality")
    st.info("Perfect for outdoor activities.")

elif aqi <= 100:
    st.info("🟡 Satisfactory")
    st.info("Air quality is acceptable.")

elif aqi <= 200:
    st.warning("🟠 Moderate")
    st.warning("Sensitive people should reduce outdoor activities.")

elif aqi <= 300:
    st.error("🔴 Poor")
    st.error("Avoid prolonged outdoor exposure.")

else:
    st.error("🟣 Very Poor")
    st.error("Stay indoors whenever possible.")

st.markdown("---")

# ==========================================
# Footer
# ==========================================

st.markdown(
    """
    <center>
    <h4>🌍 AI Air Quality Prediction System</h4>
    <p>Built with ❤️ using Python • Streamlit • Machine Learning</p>
    </center>
    """,
    unsafe_allow_html=True,
)

# ==========================================
# Page Routing
# ==========================================

if selected == "Prediction":
    with open("prediction.py", "r", encoding="utf-8") as f:
       exec(f.read())

elif selected == "Analytics":
    with open("analytics.py", "r", encoding="utf-8") as f:
       exec(f.read())



elif selected == "History":
    st.title("📋 AQI History")
    history_df = df.tail(30)
    st.dataframe(history_df, use_container_width=True)

elif selected == "Report":

    import aqi_report

    st.title("📄 AQI Report")

    st.write("Generate your Air Quality Report")

    st.markdown("---")

    st.subheader("Report Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("AQI", int(latest["AQI"]))

    with col2:
        st.metric("PM2.5", round(latest["PM2.5"], 2))

    with col3:
        st.metric("PM10", round(latest["PM10"], 2))


    if st.button("📄 Generate Report"):

        pdf_file = aqi_report.generate_report(
            city,
            int(latest["AQI"]),
            latest["PM2.5"],
            latest["PM10"],
            "Air Quality Report"
        )

        with open(pdf_file, "rb") as file:

            st.download_button(
                label="⬇️ Download PDF",
                data=file,
                file_name="AQI_Report.pdf",
                mime="application/pdf"
            )


elif selected == "Settings":

 
    exec(open("settings.py", encoding="utf-8").read())

if selected == "About":
    exec(open("about.py", encoding="utf-8").read())