# FastAPI FIPE Data Loader

This project is a FastAPI application that interacts with the FIPE (Fundação Instituto de Pesquisas Econômicas) API to load vehicle data into a database. It provides endpoints to load vehicle brand data from FIPE and access them through APIs.

### Build

To build the Docker images for the server API and Celery worker:

```bash
make build
```

This command will build the server API and Celery worker Docker images using the provided Dockerfiles.

## Running with kubernetes (Minikube)

To run the project using Minikube:

```bash
make run
```

This command starts Minikube, sets up the necessary environment, applies the Kubernetes deployment and service configurations, and opens the Minikube dashboard.

### Stop

To stop the project and Minikube:

```bash
make stop
```

## Running with Docker Compose

To run the project using Docker Compose:

```bash
make run-compose
```

This command stops the Minikube cluster.

