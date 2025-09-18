FROM python:slim

ENV PYTHONDONOTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 

WORKDIR /app

# System deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.cargo/bin:$PATH"

# Copy only dependency files first for caching
COPY pyproject.toml requirements.txt* ./
RUN uv pip install --system --no-cache -r requirements.txt || true

# Copy the rest of the app
COPY . .

# Train (optional — might make image very heavy)
RUN python pipeline/training_pipeline.py

EXPOSE 5000
CMD ["python", "application.py"]
