FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -U pip \
    && pip install --no-cache-dir -r requirements/production.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
