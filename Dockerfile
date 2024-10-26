FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt .
COPY . /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python3", "app.py"]