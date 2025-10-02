"""
Quick script to retrain model with current scikit-learn version
Run this locally and commit the new model file
"""
import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load and process data
df = pd.read_csv("backend/Hotel_Reservations.csv")

# Same preprocessing as original
df = df.drop("Booking_ID", axis=1)
df["total_nights"] = df["no_of_week_nights"] + df["no_of_weekend_nights"]
df = df.drop(["no_of_week_nights", "no_of_weekend_nights"], axis=1)
df["lead_time"] = np.log1p(df["lead_time"])
df["avg_price_per_room"] = np.log1p(df["avg_price_per_room"])

# Encode categoricals
categorical_cols = df.select_dtypes(include=["object", "category"]).columns.drop("booking_status")
df = pd.get_dummies(df, columns=categorical_cols)

# Split data
X = df.drop("booking_status", axis=1)
y = df["booking_status"]
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Train model
model = RandomForestClassifier(n_estimators=300, max_depth=15, min_samples_split=5, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "hotel_model.pkl")
joblib.dump(model, "backend/hotel_model.pkl")
print("✅ Model retrained and saved with current scikit-learn version!")
print(f"✅ Model accuracy: {model.score(X_val, y_val):.3f}")
