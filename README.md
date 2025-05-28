# 🚀 FastAPI Auth API

This project is a clean, modular authentication system built with **FastAPI**, supporting user registration, login, and token management. It uses an asynchronous stack with modern best practices: SQLAlchemy 2.0, Pydantic v2, Alembic for migrations, and Dependency Injection.

---

## 📦 Tech Stack

* **Python 3.11+**
* **FastAPI**
* **SQLAlchemy 2.0 (async)**
* **Pydantic v2**
* **Alembic**
* **Passlib (bcrypt)**
* **PostgreSQL (recommended)**

---

## 🔐 Features

* User registration with password hashing
* Token generation with expiration
* Login with credential validation
* Clean architecture (services, repositories, schemas, etc.)
* Alembic migration support
* Fully typed and modular

---

## 📁 Project Structure

```
fastapi_app/
├── api/                # Routers
│   └── v1/
│       └── auth/       # /register and /login endpoints
├── core/               # Settings and configuration
├── models/             # SQLAlchemy models
├── schemas/            # Pydantic schemas
├── services/           # Business logic
├── repos/              # Database access layer
├── alembic/            # Database migrations
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Stalkies/FastAPI-base-Template.git
cd FastAPI-base-Template
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Or using [uv](https://github.com/astral-sh/uv):

```bash
uv pip install
```

### 3. Setup environment variables

Create `.env` file and set your database URL and other configs:

```
DATABASE__URL=postgresql+asyncpg://user:password@localhost/db_name
```

### 4. Run migrations

```bash
alembic upgrade head
```

### 5. Run the app

```bash
uvicorn fastapi_app.main:app --reload
```

---

## 📩 API Endpoints

| Method | Path                    | Description            |
| ------ | ----------------------- | ---------------------- |
| POST   | `/api/v1/auth/register` | Register a new user    |
| POST   | `/api/v1/auth/login`    | Log in and get a token |

---

## ✅ TODO / Improvements

* Add token revocation and logout
* JWT-based token alternative
* Role-based permissions
* User profile endpoint
* Swagger UI enhancements

---

## 📄 License

MIT License © 2025 Oleksandr Bulanov
