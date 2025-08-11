ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:latest
FROM ${BUILD_FROM}

# Install dependencies
RUN apk add --no-cache python3 py3-pip bash curl ffmpeg

# Create work directory
WORKDIR /app

# Copy app files
COPY run.sh /run.sh
COPY megan.py /app/megan_ai.py

# Make run script executable
RUN chmod a+x /run.sh

# Install Python dependencies in a venv
RUN python3 -m venv /venv && \
    . /venv/bin/activate && \
    pip install --no-cache-dir --upgrade pip wheel setuptools && \
    pip install --no-cache-dir fastapi uvicorn openai

# Set environment
ENV PATH="/venv/bin:$PATH"

# Run
CMD [ "/bin/bash", "/run.sh" ]
