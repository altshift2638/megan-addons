#!/usr/bin/env bash
echo "[Megan] Starting ChatGPT server..."
exec uvicorn megan_ai:app --host 0.0.0.0 --port 8000
