FROM python:3.10.4-alpine3.14

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./ /app