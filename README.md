# ScaleTrack – Logistics Tracking Bot

A real-time, multi-carrier logistics tracking bot with compressed shipment data
supporting global and Indian courier services.

## Features
- Real-time shipment tracking
- Supports 1000+ packages
- Indian + International carriers
- 75% data compression (ScaleDown)
- Delivery ETA prediction
- WebSocket live updates

## Tech Stack
- Python (FastAPI)
- Redis
- WebSockets
- Carrier APIs

## Run Locally
```bash
cp .env.example .env
pip install -r requirements.txt
uvicorn app.main:app --reload
