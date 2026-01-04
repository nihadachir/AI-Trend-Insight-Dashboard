from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI(title="Sentiment API")

class Payload(BaseModel):
    text: str

sentiment_model = pipeline("sentiment-analysis")

@app.post("/sentiment")
def analyze(payload: Payload):
    result = sentiment_model(payload.text)[0]
    return {
        "sentiment": result["label"],
        "score": float(result["score"])
    }
