import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report

# --------------------------
# 1. Load Data
# --------------------------
df = pd.read_csv("Hotel_Reservations.csv")

# --------------------------
# 2. Feature Engineering
# --------------------------
# Drop Booking_ID (not useful)
df = df.drop("Booking_ID", axis=1)

# Combine correlated features
df["total_nights"] = df["no_of_week_nights"] + df["no_of_weekend_nights"]
df = df.drop(["no_of_week_nights", "no_of_weekend_nights"], axis=1)

# Handle skewed features with log transform
df["lead_time"] = np.log1p(df["lead_time"])
df["avg_price_per_room"] = np.log1p(df["avg_price_per_room"])

# --------------------------
# 3. Encode Categorical Columns
# --------------------------
categorical_cols = df.select_dtypes(include=["object", "category"]).columns.drop("booking_status")
df = pd.get_dummies(df, columns=categorical_cols)

# --------------------------
# 4. Split Features and Target
# --------------------------
X = df.drop("booking_status", axis=1)
y = df["booking_status"]

X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# --------------------------
# 5. Train Random Forest Model
# --------------------------
model = RandomForestClassifier(
    n_estimators=300,
    max_depth=15,
    min_samples_split=5,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

# --------------------------
# 6. Evaluate Model
# --------------------------
y_pred = model.predict(X_val)

print("Accuracy:", accuracy_score(y_val, y_pred))
print("Precision:", precision_score(y_val, y_pred, pos_label="Canceled"))
print("Recall:", recall_score(y_val, y_pred, pos_label="Canceled"))
print("\nClassification Report:\n", classification_report(y_val, y_pred))

# --------------------------
# 7. Save Model
# --------------------------
joblib.dump(model, "hotel_model.pkl")
print("✅ Model saved as hotel_model.pkl")
