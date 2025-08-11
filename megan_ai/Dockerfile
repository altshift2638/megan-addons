ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:latest
FROM ${BUILD_FROM}

RUN apk add --no-cache python3 py3-pip bash curl

RUN python3 -m venv /venv \
 && . /venv/bin/activate \
 && pip install --no-cache-dir --upgrade pip wheel setuptools \
 && pip install --no-cache-dir fastapi uvicorn openai httpx

ENV PATH="/venv/bin:$PATH"
WORKDIR /app

COPY run.sh /run.sh
COPY megan_ai.py /app/megan_ai.py
RUN chmod +x /run.sh && sed -i 's/\r$//' /run.sh

EXPOSE 8000
CMD ["/run.sh"]
