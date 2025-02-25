from fastapi import FastAPI
import joblib
import numpy as np
import pandas as pd
import os

app = FastAPI()

# 절대 경로로 모델 로드
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
model = joblib.load(model_path)

@app.get("/")
def home():
    return {"message": "ML 모델 API 입니다."}

@app.post("/predict/")
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return {"prediction": int(prediction[0])}
