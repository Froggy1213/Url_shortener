# URL Shortener API

A simple and efficient URL shortening service built with **Python**, **FastAPI**, and **PostgreSQL**. The application is fully containerized using **Docker**.

## 🛠 Tech Stack

* **Python 3.11**
* **FastAPI** - High-performance web framework for building APIs.
* **SQLAlchemy** - SQL Toolkit and Object Relational Mapper (ORM).
* **PostgreSQL** - Relational database system.
* **Docker & Docker Compose** - For containerization and orchestration.
* **Pydantic** - Data validation using Python type hints.

## 🚀 Features

* **Shorten URL:** Generate a short unique key for a long URL.
* **Redirection:** Redirect incoming requests from the short key to the original URL.
* **Data Persistence:** Uses PostgreSQL to store links.
* **Containerized:** Runs easily with a single Docker command.

## ⚙️ How to Run

### Prerequisites
Make sure you have [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/install/) installed on your machine.

### 1. Clone the repository
```bash
git clone [https://github.com/Froggy1213/url-shortener-fastapi.git](https://github.com/Froggy1213/url-shortener-fastapi.git)
cd url-shortener-fastapi
```

### 2. Configure Environment
```bash
Create a .env file in the root directory:


touch .env

Add the following configuration to the .env file:
Ini, TOML

DATABASE_URL=postgresql://postgres:postgres@db:5432/shortener_db
```

### 3. Run with Docker

Build and start the containers:

```bash
docker compose up --build
```
The server will start at http://localhost:8000.
📖 API Documentation

FastAPI provides automatic interactive documentation. Once the app is running, open your browser and navigate to:

    Swagger UI: http://127.0.0.1:8000/docs

    ReDoc: http://127.0.0.1:8000/redoc

### Usage Example

### 1. Create a short link:

curl -X 'POST' \
  '[http://127.0.0.1:8000/url](http://127.0.0.1:8000/url)' \
  -H 'Content-Type: application/json' \
  -d '{
  "target_url": "[https://www.google.com](https://www.google.com)"
}'

Response:
JSON

{
  "target_url": "[https://www.google.com](https://www.google.com)",
  "key": "A1b2C",
  "is_active": true
}

###  2. Access the short link: Open http://127.0.0.1:8000/A1b2C in your browser, and you will be redirected to Google.


### 📂 Project Structure
Plaintext
```Bash
.
├── app
│   ├── crud.py        # Database CRUD operations
│   ├── database.py    # Database connection logic
│   ├── main.py        # API Endpoints
│   ├── models.py      # SQLAlchemy models
│   └── schemas.py     # Pydantic schemas
├── docker-compose.yml # Docker services config
├── Dockerfile         # Docker image build instructions
├── requirements.txt   # Python dependencies
└── README.md

```