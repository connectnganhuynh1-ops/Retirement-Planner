FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src ./src
COPY .env.example .env

# Fix Python import path
ENV PYTHONPATH=/app

EXPOSE 8080

CMD ["python", "src/app.py"]

