#!/usr/bin/env bash
set -euo pipefail

MODEL_ID="${MODEL_ID:-llama3.2:3b}"
PRELOAD_MODEL="${PRELOAD_MODEL:-true}"

if ! pgrep -x "ollama" >/dev/null; then
  echo "[Megan] Starting Ollama..."
  /usr/local/bin/ollama serve &
  sleep 3
fi

if [ "${PRELOAD_MODEL}" = "true" ]; then
  echo "[Megan] Pulling model ${MODEL_ID}..."
  /usr/local/bin/ollama pull "${MODEL_ID}" || true
fi

APP="/config/megan_ai_single_file.py"
if [ ! -f "$APP" ]; then
  APP="/opt/megan/megan_ai_single_file.py"
fi

export PROVIDER=ollama
export MODEL_ID="${MODEL_ID}"
export EMBED_MODEL_ID="nomic-embed-text"
export OLLAMA_HOST="http://localhost:11434"

echo "[Megan] Launching server..."
exec uvicorn megan_ai_single_file:app --host 0.0.0.0 --port 8000 --app-dir "$(dirname "$APP")"
