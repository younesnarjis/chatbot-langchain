FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

COPY pytest.ini .

RUN apt-get update && \
    apt-get install -y ffmpeg curl git && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY . .

ENV PYTHONPATH=/app:$PYTHONPATH

# CMD ["run.handler"]

CMD [ "python", "run.py" ]