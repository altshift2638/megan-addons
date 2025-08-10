# Megan AI (Local) — Home Assistant Add-on

Runs **Ollama** with `llama3.2:3b` and the **Megan FastAPI** server. Web UI at `http://<HA>:8000/demo`.

## Install
1. Publish this repo to GitHub (see root `repository.json`).
2. In Home Assistant: **Settings → Add-ons → Add-on Store → ⋮ → Repositories → Add** your repo URL.
3. Install **Megan AI (Local)** → **Start**.

## Override the server
Copy `server-example/megan_ai_single_file.py` from the master zip into Home Assistant’s **/config** folder to load a full server (voice + avatar).
