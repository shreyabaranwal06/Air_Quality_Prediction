import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv("dataset/clean_air_quality.csv")

# ==========================================
# Page Title
# ==========================================

st.title("📊 Air Quality Analytics")
st.write("Detailed Air Quality Analysis Dashboard")

st.markdown("---")

# ==========================================
# KPI Cards
# ==========================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📁 Total Records",
        len(df)
    )

with col2:
    st.metric(
        "🏙 Cities",
        df["City"].nunique()
    )

with col3:
    st.metric(
        "🌍 Average AQI",
        round(df["AQI"].mean(), 1)
    )

with col4:
    st.metric(
        "🚨 Maximum AQI",
        int(df["AQI"].max())
    )

st.markdown("---")

# ==========================================
# Top 10 Polluted Cities + Monthly AQI Trend
# ==========================================

left, right = st.columns(2)

# -------------------------
# Top 10 Polluted Cities
# -------------------------

with left:

    st.subheader("🏭 Top 10 Polluted Cities")

    top10 = (
        df.groupby("City")["AQI"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        top10,
        x="AQI",
        y="City",
        orientation="h",
        color="AQI",
        color_continuous_scale="Reds",
        template="plotly_dark",
        text="AQI"
    )

    fig.update_layout(
        paper_bgcolor="#0B1120",
        plot_bgcolor="#0B1120",
        font=dict(color="white"),
        height=450,
        yaxis=dict(categoryorder="total ascending"),
        coloraxis_showscale=False,
        margin=dict(l=10, r=10, t=20, b=10)
    )

    st.plotly_chart(fig, use_container_width=True)


# -------------------------
# Monthly AQI Trend
# -------------------------

with right:

    st.subheader("📈 Monthly AQI Trend")

    monthly = df.copy()

    monthly["Date"] = pd.to_datetime(monthly["Date"])

    monthly["Month"] = monthly["Date"].dt.strftime("%b")

    monthly = (
        monthly.groupby("Month")["AQI"]
        .mean()
        .reset_index()
    )

    month_order = [
        "Jan","Feb","Mar","Apr","May","Jun",
        "Jul","Aug","Sep","Oct","Nov","Dec"
    ]

    monthly["Month"] = pd.Categorical(
        monthly["Month"],
        categories=month_order,
        ordered=True
    )

    monthly = monthly.sort_values("Month")

    fig = px.line(
        monthly,
        x="Month",
        y="AQI",
        markers=True,
        template="plotly_dark"
    )

    fig.update_traces(
        line=dict(color="#00E5FF", width=4)
    )

    fig.update_layout(
        paper_bgcolor="#0B1120",
        plot_bgcolor="#0B1120",
        font=dict(color="white"),
        height=450,
        margin=dict(l=10, r=10, t=20, b=10),
        xaxis_title="",
        yaxis_title="Average AQI"
    )

    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ==========================================
# AQI Category Distribution
# ==========================================

left, right = st.columns(2)

with left:

    st.subheader("🥧 AQI Category Distribution")

    category = df["AQI_Bucket"].value_counts()

    fig = go.Figure(
        data=[
            go.Pie(
                labels=category.index,
                values=category.values,
                hole=0.55
            )
        ]
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0B1120",
        height=450
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    st.subheader("📊 Pollutant Comparison")

    latest = df.iloc[-1]

    pollutant = pd.DataFrame({

        "Pollutant":[
            "PM2.5",
            "PM10",
            "NO2",
            "SO2",
            "CO",
            "O3"
        ],

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
        pollutant,
        x="Pollutant",
        y="Value",
        color="Value",
        text="Value",
        template="plotly_dark"
    )

    fig.update_layout(
        paper_bgcolor="#0B1120",
        plot_bgcolor="#0B1120",
        font=dict(color="white"),
        height=450
    )

    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ==========================================
# AQI Gauge + City Analysis
# ==========================================

left, right = st.columns([2, 1])

with left:

    st.subheader("🌍 Current AQI Gauge")

    latest = df.iloc[-1]

    fig = go.Figure(go.Indicator(

        mode="gauge+number",

        value=float(latest["AQI"]),

        title={"text": "Current AQI"},

        gauge={

            "axis": {"range": [0, 500]},

            "bar": {"color": "deepskyblue"},

            "steps": [

                {"range": [0, 50], "color": "green"},

                {"range": [50, 100], "color": "yellow"},

                {"range": [100, 200], "color": "orange"},

                {"range": [200, 300], "color": "red"},

                {"range": [300, 500], "color": "purple"}

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

    st.subheader("📌 AQI Statistics")

    st.metric("Minimum AQI", int(df["AQI"].min()))

    st.metric("Average AQI", round(df["AQI"].mean(), 2))

    st.metric("Maximum AQI", int(df["AQI"].max()))

    st.metric("Median AQI", round(df["AQI"].median(), 2))

st.markdown("---")

# ==========================================
# City Wise Average AQI + Dataset Summary
# ==========================================

left, right = st.columns(2)

# --------------------------------
# City Wise Average AQI
# --------------------------------

with left:

    st.subheader("🏙️ City Wise Average AQI")

    city_avg = (
        df.groupby("City")["AQI"]
        .mean()
        .round(1)
        .reset_index()
        .sort_values("AQI", ascending=False)
    )

    fig = px.bar(
        city_avg.head(10),
        x="City",
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
        height=420,
        xaxis_title="City",
        yaxis_title="Average AQI",
        coloraxis_showscale=False
    )

    st.plotly_chart(fig, use_container_width=True)


# ==========================================
# Dataset Summary (KPI Cards)
# ==========================================

with right:

    st.subheader("📋 Dataset Summary")

    c1, c2 = st.columns(2)

    with c1:
        st.metric("📄 Total Records", len(df))
        st.metric("🌍 Total Cities", df["City"].nunique())
        st.metric("📈 Average AQI", round(df["AQI"].mean(), 2))
        st.metric("🔥 Maximum AQI", int(df["AQI"].max()))

    with c2:
        st.metric("🌱 Minimum AQI", int(df["AQI"].min()))
        st.metric("💨 Avg PM2.5", round(df["PM2.5"].mean(), 2))
        st.metric("🌫 Avg PM10", round(df["PM10"].mean(), 2))
        st.metric("🧪 Avg NO₂", round(df["NO2"].mean(), 2))
st.markdown("---")

# ==========================================
# Recent Dataset Records
# ==========================================

st.subheader("📄 Latest 5 Records")

latest_records = df.tail(5)

st.dataframe(
    latest_records,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# ==========================================
# Air Quality Insights
# ==========================================

st.subheader("💡 Air Quality Insights")

highest_city = city_avg.iloc[0]["City"]
highest_aqi = round(city_avg.iloc[0]["AQI"], 1)

lowest_city = city_avg.iloc[-1]["City"]
lowest_aqi = round(city_avg.iloc[-1]["AQI"], 1)

col1, col2 = st.columns(2)

with col1:
    st.success(f"""
### 🌍 Best Air Quality

**City:** {lowest_city}

**Average AQI:** {lowest_aqi}
""")

with col2:
    st.error(f"""
### 🚨 Most Polluted City

**City:** {highest_city}

**Average AQI:** {highest_aqi}
""")

st.markdown("---")

