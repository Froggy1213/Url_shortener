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