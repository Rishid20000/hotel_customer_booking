from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np
from flask_cors import CORS


app = Flask(__name__)

CORS(app)

# Load trained model
model = joblib.load("hotel_model.pkl")

# Expected features (order matters!)
expected_features = [
    "no_of_adults",
    "no_of_children",
    "total_nights",
    "lead_time",
    "avg_price_per_room",
    "room_type_reserved",
    "type_of_meal_plan",
    "market_segment_type",
    "repeated_guest",
    "no_of_special_requests"
]

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json  # Get JSON from frontend
        df = pd.DataFrame([data])

        # Preprocessing same as training
        df["lead_time"] = np.log1p(df["lead_time"])
        df["avg_price_per_room"] = np.log1p(df["avg_price_per_room"])

        # Encode categoricals (align with training)
        df = pd.get_dummies(df)
        # Align columns with training data
        import pickle
        # Align with training columns
        training_cols = model.feature_names_in_
        df = df.reindex(columns=training_cols, fill_value=0)

        # Predict
        prediction = model.predict(df)[0]

        return jsonify({"prediction": prediction})
    except Exception as e:
        return jsonify({"error": str(e) })

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
