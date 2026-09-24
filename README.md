# Air Quality Prediction

A web application that helps users explore air quality data, understand pollution trends, and generate air quality predictions. Built with Python and Streamlit, it combines an interactive dashboard, data visualizations, machine learning, and downloadable PDF reports.

## Overview

Air pollution data can be difficult to understand when it is presented only as numbers. This project makes it easier to explore important indicators such as AQI, PM2.5, and PM10 through a simple, interactive interface.

Users can select a city, review its air quality information, explore visual trends, use the prediction feature, and download a summary report.

## Features

- **Interactive dashboard:** Displays key air quality metrics for the selected city.
- **City-wise analysis:** Allows users to explore available data for different cities.
- **AQI prediction:** Uses a trained machine learning model to generate predictions.
- **Visual analytics:** Presents pollution comparisons and AQI trends through interactive charts.
- **PDF report generation:** Creates a downloadable report with air quality details.
- **Settings page:** Provides options to customize the application experience.

## Tech Stack

| Purpose | Technologies |
| --- | --- |
| Programming language | Python |
| Web application | Streamlit |
| Data processing | Pandas |
| Data visualization | Plotly |
| Machine learning | scikit-learn |
| Model storage | joblib |
| PDF generation | ReportLab |

## Project Structure

```text
Air_Quality_Prediction/
├── app.py
├── dashboard.py
├── prediction.py
├── analytics.py
├── aqi_report.py
├── settings.py
├── about.py
├── utils.py
├── train_model.py
├── dataset/
│   └── clean_air_quality.csv
└── requirements.txt
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Air_Quality_Prediction.git
cd Air_Quality_Prediction
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Or on macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the model

```bash
python train_model.py
```

The trained model file is not stored in the repository due to its size. Run the training script before using the prediction feature.

### 5. Start the application

```bash
streamlit run app.py
```

Streamlit will display a local URL in the terminal. Open it in your browser to use the application.

## What I Learned

This project helped me work with air quality datasets, prepare data for analysis, build interactive visualizations, integrate a machine learning model into a web application, and generate downloadable PDF reports.

## Future Scope

- Support more cities and updated datasets.
- Compare the performance of different prediction models.
- Add more detailed analysis of individual pollutants.

**Live App:** [Open Air Quality Prediction Dashboard](https://shreya-air-quality-prediction.streamlit.app/)

## Author

**Shreya Baranwal**  
Final-year B.Tech student in Computer Science and Engineering (Artificial Intelligence)

Github: https://github.com/shreyabaranwal06
