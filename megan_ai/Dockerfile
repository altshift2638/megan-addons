ARG BUILD_FROM=ghcr.io/hassio-addons/base:16.3.3
FROM ${BUILD_FROM}

RUN apk add --no-cache python3 py3-pip git curl bash ca-certificates ffmpeg

# Use a venv (PEP 668 compliant)
RUN python3 -m venv /venv \
 && . /venv/bin/activate \
 && pip install --no-cache-dir --upgrade pip wheel setuptools \
 && pip install --no-cache-dir fastapi uvicorn httpx numpy soundfile TTS

ENV PATH="/venv/bin:$PATH"

# Install Ollama
RUN curl -fsSL https://ollama.com/download/linux | sh || true
ENV OLLAMA_HOST=0.0.0.0:11434

WORKDIR /opt/megan
# Placeholder server (we'll copy a ready example you can drop into /config)
RUN printf '%s\n' '# Placeholder; copy megan_ai_single_file.py into /config to override' > /opt/megan/megan_ai_single_file.py

COPY rootfs /

EXPOSE 8000 11434
CMD ["/run.sh"]
