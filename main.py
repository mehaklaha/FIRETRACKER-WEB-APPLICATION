from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from model import predict_fire_risk
from database import insert_fire_data, fetch_fire_data

# FastAPI app creation
app = FastAPI(
    title="Fire Tracker API",
    description="Predictive fire risk analysis and visualization",
    version="1.0"
)

# ADD CORS MIDDLEWARE HERE (RIGHT AFTER app = FastAPI)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://firetrackerweb.netlify.app/"],  # Replace with Netlify URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "FireTracker API is running"}


# Request model
class FireInput(BaseModel):
    latitude: float
    longitude: float
    temperature: float
    humidity: float
    wind_speed: float
    vegetation: float

# Predict fire risk
@app.post("/predict")
def predict_fire(data: FireInput):
    risk = predict_fire_risk([
        data.temperature,
        data.humidity,
        data.wind_speed,
        data.vegetation
    ])

    insert_fire_data(
        data.latitude,
        data.longitude,
        risk
    )

    return {"fire_risk_percentage": risk}

# Fetch stored fire data
@app.get("/fires")
def get_fires():
    return fetch_fire_data()