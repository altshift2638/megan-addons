ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:latest
FROM ${BUILD_FROM}

# Base + Python venv
RUN apk add --no-cache python3 py3-pip bash curl  && python3 -m venv /venv  && . /venv/bin/activate  && pip install --no-cache-dir --upgrade pip wheel setuptools  && pip install --no-cache-dir fastapi uvicorn openai httpx pydantic

ENV PATH="/venv/bin:$PATH"
WORKDIR /app

# App code
COPY server.py /app/server.py

# s6 service (let /init PID1 manage it)
COPY rootfs/ /

# Ensure service run script is executable and has unix line endings
RUN chmod +x /etc/services.d/megan/run  && sed -i 's/\r$//' /etc/services.d/megan/run

EXPOSE 8000
