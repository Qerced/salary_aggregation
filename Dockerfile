FROM python:3.11-slim

WORKDIR /salary_aggregation
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir
CMD ["python3", "app/main.py"]
