FROM python:3.8

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    torch \
    transformers \
    python-telegram-bot

RUN git clone https://github.com/huggingface/transformers.git

WORKDIR /app

COPY . .

CMD ["python", "bot.py"]
