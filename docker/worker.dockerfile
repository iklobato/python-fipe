FROM python:3.8

WORKDIR /app

RUN pip install celery[redis]==5.2.7

COPY broker/ .
