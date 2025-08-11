ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:latest
FROM ${BUILD_FROM}

# Base + Python venv + jq (fallback path)
RUN apk add --no-cache python3 py3-pip bash curl jq \
 && python3 -m venv /venv \
 && . /venv/bin/activate \
 && pip install --no-cache-dir --upgrade pip wheel setuptools \
 && pip install --no-cache-dir fastapi uvicorn openai httpx pydantic

ENV PATH="/venv/bin:$PATH"
WORKDIR /app

# App code
COPY server.py /app/server.py

# s6 service files
COPY rootfs/ /

# Ensure service script is executable, LF endings
RUN chmod +x /etc/services.d/megan/run \
 && sed -i 's/\r$//' /etc/services.d/megan/run

EXPOSE 8000
# NOTE: no CMD here — Home Assistant's /init (s6) is PID 1 and will start our service
