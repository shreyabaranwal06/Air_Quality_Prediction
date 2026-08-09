import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# ===============================
# Load Clean Dataset
# ===============================
df = pd.read_csv("dataset/clean_air_quality.csv")

# ===============================
# Features & Target
# ===============================
X = df[[
    "PM2.5",
    "PM10",
    "NO2",
    "SO2",
    "CO",
    "O3"
]]

y = df["AQI"]

# ===============================
# Train Test Split
# ===============================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ===============================
# Train Model
# ===============================
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# ===============================
# Prediction
# ===============================
prediction = model.predict(X_test)

# ===============================
# Accuracy
# ===============================
print("="*50)
print("MODEL PERFORMANCE")
print("="*50)

print("R2 Score :", round(r2_score(y_test, prediction),3))
print("MAE :", round(mae := mean_absolute_error(y_test, prediction),2))

# ===============================
# Save Model
# ===============================
joblib.dump(model, "model/aqi_model.pkl")

print("\n✅ Model Saved Successfully!")
