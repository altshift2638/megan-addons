#!/usr/bin/env bash
set -e
echo "[Megan] Starting ChatGPT backend..."
exec uvicorn server:app --host 0.0.0.0 --port 8000
