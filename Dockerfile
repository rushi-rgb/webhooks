
FROM python:3.8-slim

WORKDIR /app

COPY . /app

EXPOSE 8080

ENV NAME World

CMD ["python", "app.py"]

echo "Hello From KUCL"
