
# FIPE API Kafka worker

This project provides a FastAPI-based API for fetching vehicle information using the FIPE service. It includes workers for fetching vehicle brands (marcas), models (modelos), years (anos), and values (valor) from the FIPE service. Kafka is used for managing asynchronous tasks and communication.

## Setup

1. Clone this repository to your local machine.
2. Install the required dependencies using:
   ```bash
   pip install -r requirements.txt
   ```
3. Update the configuration in `config.py` to match your environment settings, such as FIPE API endpoints and Kafka connection details.

## Running the API

To run the API, execute the following command:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

The API will be accessible at `http://localhost:8000`.

## Endpoints

- `GET /api/fipe/marcas`: Fetches vehicle brands from the FIPE service.
- `GET /`: A simple health check endpoint returning the status as "ok".

## Workers and Kafka

The API utilizes workers for asynchronous data fetching from the FIPE service. Kafka is used to manage and coordinate these workers. Each worker corresponds to a specific type of data (marcas, modelos, anos, valor).
