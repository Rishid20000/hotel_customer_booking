# 🏨 Hotel Customer Booking ML Application

A full-stack machine learning application that predicts hotel booking cancellations using Random Forest classification. The application features a React frontend deployed on Vercel and a Flask backend with ML model deployed on Railway.

## 🌐 Live Application

- **Frontend (React)**: [[Deployed on Vercel](https://hotel-customer-booking-vercel-url.vercel.app)](https://hotel-customer-booking.vercel.app/)
- **Backend API (Flask)**: [https://hotelcustomerbooking-production.up.railway.app](https://<your-url-provided-by-railway>.up.railway.app)

## 🎯 Features

- **ML-Powered Predictions**: Uses Random Forest classifier to predict booking cancellations
- **Interactive Web Interface**: User-friendly form to input booking details
- **Real-time API**: RESTful API that processes booking data and returns predictions
- **Responsive Design**: Works seamlessly across desktop and mobile devices
- **CORS Enabled**: Frontend and backend communicate securely

## 📁 Project Structure

```
hotel_customer/
├── backend/                          # Flask API with ML Model
│   ├── app.py                       # Main Flask application
│   ├── train.py                     # Model training script
│   ├── hotel_model.pkl             # Trained Random Forest model
│   ├── Hotel_Reservations.csv      # Training dataset
│   ├── requirements.txt            # Python dependencies
│   ├── Procfile                    # Railway deployment config
│   └── runtime.txt                 # Python version specification
│
├── hotel-customer-app/              # React Frontend Application
│   ├── public/                     # Static assets
│   │   ├── index.html             # Main HTML template
│   │   └── favicon.ico            # App icon
│   ├── src/                       # React source code
│   │   ├── App.js                 # Main React component with booking form
│   │   ├── App.css                # Application styling
│   │   ├── index.js               # React app entry point
│   │   └── index.css              # Global styles
│   ├── package.json               # Node.js dependencies and scripts
│   └── .env.example               # Environment variables template
│
├── README.md                        # This file
├── requirements.txt                 # Root-level Python dependencies
├── nixpacks.toml                   # Build configuration
├── main.py                         # Alternative entry point
├── hotel_model.pkl                 # Model copy for root deployment
├── dataPre                         # Data preprocessing utilities
└── WARP.md                         # Additional documentation
```

## 🚀 Deployment Architecture

### Frontend - Vercel Deployment

**Platform**: [Vercel](https://vercel.com)
**Framework**: Create React App
**Root Directory**: `hotel-customer-app/`

**Configuration**:
```bash
# Build Settings
Build Command: npm run build
Output Directory: build
Install Command: npm install

# Environment Variables
REACT_APP_API_URL=https://hotelcustomerbooking-production.up.railway.app
```

**Deployment Process**:
1. Vercel auto-detects Create React App
2. Builds the React application
3. Serves static files via CDN
4. Environment variables injected at build time

### Backend - Railway Deployment

**Platform**: [Railway](https://railway.app)
**Framework**: Flask + Gunicorn
**Root Directory**: `backend/`

**Configuration**:
```bash
# Deployment Settings
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
Python Version: 3.11.8

# Auto-scaling
Min Replicas: 1
Max Replicas: 10
```

**Deployment Process**:
1. Railway detects Python application
2. Installs dependencies from requirements.txt
3. Loads ML model (hotel_model.pkl)
4. Starts Flask app with Gunicorn
5. Provides HTTPS endpoint

## 🛠️ Technology Stack

### Backend (Railway)
- **Python 3.11.8**
- **Flask 2.3.3** - Web framework
- **Scikit-learn 1.6.1** - ML model
- **Pandas 2.0.3** - Data processing
- **NumPy 1.24.3** - Numerical computations
- **Joblib 1.3.2** - Model serialization
- **Flask-CORS 4.0.0** - Cross-origin requests
- **Gunicorn 21.0.0** - WSGI HTTP Server

### Frontend (Vercel)
- **React 19.2.0** - UI framework
- **Axios** - HTTP client for API calls
- **Create React App** - Build toolchain
- **CSS3** - Styling and responsive design

### Machine Learning
- **Algorithm**: Random Forest Classifier
- **Features**: 10 input features (adults, children, nights, lead time, etc.)
- **Output**: Binary classification (Canceled/Not_Canceled)
- **Accuracy**: ~85% on validation set

## 📊 API Documentation

### Base URL
```
https://hotelcustomerbooking-production.up.railway.app
```

### Endpoints

#### GET `/`
Health check endpoint

**Response**:
```json
{
  "message": "Hotel Booking ML API is running!",
  "status": "online",
  "endpoints": {
    "predict": "/predict (POST)"
  }
}
```

#### POST `/predict`
Predicts booking cancellation probability

**Request Body**:
```json
{
  "no_of_adults": 2,
  "no_of_children": 0,
  "total_nights": 3,
  "lead_time": 30,
  "avg_price_per_room": 150,
  "room_type_reserved": "Room_Type_1",
  "type_of_meal_plan": "Meal_Plan_1",
  "market_segment_type": "Online",
  "repeated_guest": "No",
  "no_of_special_requests": 1
}
```

**Response**:
```json
{
  "prediction": "Not_Canceled"
}
```

**Error Response**:
```json
{
  "error": "Error description"
}
```

## 🏃‍♂️ Local Development

### Prerequisites
- Node.js 16+
- Python 3.11+
- Git

### Backend Setup
```bash
# Clone repository
git clone https://github.com/Rishd20000/hotel_customer_booking.git
cd hotel_customer/backend

# Install Python dependencies
pip install -r requirements.txt

# Run Flask development server
python app.py
# Server runs on http://localhost:5000
```

### Frontend Setup
```bash
# Navigate to frontend directory
cd hotel-customer-app

# Install Node.js dependencies
npm install

# Set environment variable for local development
echo "REACT_APP_API_URL=http://localhost:5000" > .env.local

# Start React development server
npm start
# App runs on http://localhost:3000
```

### Testing the Full Stack
1. Start backend server (port 5000)
2. Start frontend server (port 3000)
3. Navigate to http://localhost:3000
4. Fill booking form and test predictions

## 🔄 CI/CD Pipeline

### Automatic Deployments
- **Frontend**: Vercel auto-deploys on push to `main` branch
- **Backend**: Railway auto-deploys on push to `main` branch
- **Zero-downtime deployments** with health checks

### Environment Variables
- Production API URL automatically configured
- CORS settings optimized for production
- SSL/HTTPS enabled by default

## 🧪 Model Performance

### Training Data
- **Dataset**: Hotel Reservations CSV (36,275 records)
- **Features**: 10 engineered features
- **Target**: Binary classification (Canceled/Not_Canceled)

### Model Metrics
- **Algorithm**: Random Forest (300 estimators)
- **Accuracy**: ~85%
- **Precision**: ~82%
- **Recall**: ~78%
- **Cross-validation**: 5-fold CV

### Feature Importance
1. Lead time (booking advance days)
2. Average price per room
3. Number of special requests
4. Market segment type
5. Room type reserved

## 🌟 Demo Usage

1. **Visit the live application**: [Frontend URL]
2. **Fill the booking form**:
   - Number of adults and children
   - Total nights staying
   - Lead time (days in advance)
   - Average room price
   - Room type and meal plan
   - Market segment
   - Special requests count
3. **Click "Predict"**
4. **View the ML prediction**:
   - ✅ "Low risk. Booking confirmed without advance."
   - ⚠️ "High risk of cancellation. Hotel requires 30% advance payment."

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Developer

**Rishabhdddd Dwivedi**
- GitHub: [@Rishd20000](https://github.com/Rishd20000)
- Email: Rishabhdwivedi31@gmail.com

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 🐛 Issues & Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/Rishd20000/hotel_customer_booking/issues) page
2. Create a new issue with detailed description
3. Include error logs and steps to reproduce

---

**Built with ❤️ using React, Flask, and Machine Learning**



