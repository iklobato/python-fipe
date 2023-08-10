
# FastAPI FIPE Data Loader

This project is a FastAPI application that interacts with the FIPE (Fundação Instituto de Pesquisas Econômicas) API to load vehicle data into a database. It provides endpoints to load vehicle brand data from FIPE and access them through APIs.

## Getting Started

These instructions will help you set up and run the FastAPI application on your local machine.

### Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.7+
- Pipenv (recommended for managing dependencies)

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone <repository_url>
   cd python-fipe
   ```

2. Install project dependencies using Pipenv:

   ```bash
   pipenv install
   ```

### Configuration

1. Inside `config.py`, provide the necessary configuration values, such as `FIPE_BASE_URL`.

### Running the Application

To run the FastAPI application, follow these steps:

1. Activate the virtual environment:

   ```bash
   docker-compose up -d
 ```

1. Access the application's Swagger documentation by opening your web browser and navigating to:

   ```
   http://localhost:8000/docs
   ```

## Usage

### Loading Data

To load data from the FIPE API into the database, you can use the `/api/load` endpoint:

```
GET /api/load
```

You can provide the `limit` parameter to specify the number of data records to load. For example:
    
```
GET /api/load?limit=10
```

### Retrieving Vehicle Brands

You can retrieve vehicle brand data using the following endpoints:

1. Retrieve all vehicle brands:

   ```
   GET /api/marcas
   ```

2. Partially update vehicle brands:

   ```
   PATCH /api/marcas
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
