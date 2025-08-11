#!/bin/bash
echo "[Megan] Starting ChatGPT Megan AI..."

# Start FastAPI server
exec uvicorn megan:app --host 0.0.0.0 --port 8000
