from python:3.8-slim-buster

RUN mkdir /app
COPY k8s.py /app/k8s.py
COPY config.py /app/config.py
COPY config.yaml /app/config.yaml
COPY models.py /app/models.py

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt
