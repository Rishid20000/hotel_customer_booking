# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

Hotel Customer Booking Prediction System - A full-stack application that predicts hotel booking cancellations using machine learning. The system consists of:

- **Backend**: Flask REST API serving a trained Random Forest model
- **Frontend**: React application providing user interface for booking predictions
- **ML Pipeline**: Data processing, training, and model persistence components

## Project Structure

```
hotel_customer/
├── backend/                    # Python Flask API server
│   ├── app.py                 # Main Flask application with prediction endpoint
│   ├── train.py               # ML model training script
│   ├── downloadDataSet.py     # Kaggle dataset download utility
│   ├── hotel_model.pkl        # Trained Random Forest model (generated)
│   └── Hotel_Reservations.csv # Training dataset
└── hotel-customer-app/        # React frontend application
    ├── src/App.js             # Main component with booking form
    ├── package.json           # Node.js dependencies
    └── public/                # Static assets
```

## Development Commands

### Backend (Flask API)

From the `backend/` directory:

```bash
# Start the Flask development server
python app.py

# Train the machine learning model (generates hotel_model.pkl)
python train.py

# Download fresh dataset from Kaggle
python downloadDataSet.py
```

**Backend Dependencies** (install via pip):
- flask
- flask-cors
- joblib
- pandas
- numpy
- scikit-learn
- kagglehub

### Frontend (React App)

From the `hotel-customer-app/` directory:

```bash
# Install dependencies
npm install

# Start development server (runs on http://localhost:3000)
npm start

# Run tests
npm test

# Build for production
npm run build
```

### Full Application Startup

1. **Backend**: `cd backend && python app.py` (runs on port 5000)
2. **Frontend**: `cd hotel-customer-app && npm start` (runs on port 3000)

## Architecture Details

### Machine Learning Pipeline

- **Model**: Random Forest Classifier (300 trees, max_depth=15)
- **Target**: Predicts booking cancellation risk (Canceled/Not_Canceled)
- **Features**: 10 input features including guest details, stay duration, pricing, and preferences
- **Preprocessing**: Log transformations for skewed features (lead_time, avg_price_per_room), one-hot encoding for categoricals

Key features:
- `no_of_adults`, `no_of_children`: Guest composition
- `total_nights`: Combined weeknight + weekend stay duration
- `lead_time`: Days between booking and arrival (log-transformed)
- `avg_price_per_room`: Room pricing (log-transformed)
- Categorical: room_type, meal_plan, market_segment, repeated_guest status

### API Architecture

**POST /predict**: Main prediction endpoint
- Input: JSON with booking features
- Output: Cancellation prediction ("Canceled" or "Not_Canceled")
- CORS enabled for frontend integration

### Frontend Architecture

**Single Page Application**:
- Form-based input for all 10 prediction features
- Real-time API calls to Flask backend
- Conditional styling based on prediction results
- Loading states and error handling

## Testing & Development

### Model Retraining
- Run `python train.py` to retrain with fresh data
- Outputs accuracy, precision, recall metrics
- Automatically saves new model as `hotel_model.pkl`

### API Testing
```bash
# Test prediction endpoint
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"no_of_adults": 2, "no_of_children": 1, "total_nights": 3, "lead_time": 30, "avg_price_per_room": 150, "room_type_reserved": "Room_Type_1", "type_of_meal_plan": "Meal_Plan_1", "market_segment_type": "Online", "repeated_guest": "No", "no_of_special_requests": 1}'
```

### Common Issues

**Model Loading Errors**: Ensure `hotel_model.pkl` exists in backend directory (run `train.py` if missing)

**CORS Issues**: Flask-CORS is configured to allow all origins in development

**Feature Mismatch**: The model expects exact feature names and preprocessing - don't modify the expected_features list in `app.py` without retraining

**Data Alignment**: Training uses pandas get_dummies() - prediction endpoint must align columns with the saved model's feature_names_in_
