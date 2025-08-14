ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:latest
FROM ${BUILD_FROM}

RUN apk add --no-cache python3 py3-pip bash curl jq  && python3 -m venv /venv  && . /venv/bin/activate  && pip install --no-cache-dir --upgrade pip wheel setuptools  && pip install --no-cache-dir fastapi uvicorn openai httpx pydantic

ENV PATH="/venv/bin:$PATH"
WORKDIR /app

COPY server.py /app/server.py
COPY rootfs/ /

RUN chmod +x /etc/services.d/megan/run  && sed -i 's/\r$//' /etc/services.d/megan/run

EXPOSE 8000
