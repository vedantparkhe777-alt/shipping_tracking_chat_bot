from fastapi import FastAPI
from time import time

app = FastAPI(title="ScaleTrack")

@app.get("/")
def health():
    return {"status": "ok"}

@app.get("/track/{tracking_id}")
def track(tracking_id: str):
    return {
        "tracking_id": tracking_id,
        "status": "IN_TRANSIT",
        "location": "IN-IDR",
        "timestamp": int(time())
    }
