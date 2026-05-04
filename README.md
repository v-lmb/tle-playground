# 🛰️ tle-playground

A Python backend training project — fetching, storing, and exposing satellite TLE (Two-Line Element) data.

> **Context**: Preparatory mini-project for the [Orekit](https://www.orekit.org) website rebuild. The goal is to get comfortable with the FastAPI + PostgreSQL + SQLAlchemy stack before tackling the real thing.

---

## 📐 Project Structure

```
tle-playground/
├── app/
│   ├── __init__.py
│   ├── database.py        # PostgreSQL connection + SQLAlchemy session
│   ├── models.py          # ORM models (satellites table)
│   └── routers/
│       └── satellites.py  # FastAPI routes
├── migrations/            # Alembic migration files (Step 4)
├── ingest.py              # TLE ingestion script from Celestrak
├── main.py                # FastAPI entry point
├── alembic.ini            # Alembic config (Step 4)
├── .env                   # Environment variables (not versioned)
├── .env.example           # Environment variables template
├── requirements.txt
└── README.md
```

---

## 🗺️ Roadmap

| Step | Description | Status |
|------|-------------|--------|
| **1** | Fetch and parse TLE data from Celestrak | ✅ Done |
| **2** | Store in PostgreSQL (SQLAlchemy 2 + models) | ✅ Done |
| **3** | FastAPI hello world — `/health` and `/satellites` routes | ✅ Done |
| **4** | Alembic — schema migrations | ✅ Done |
| **5** | Cron job — automatic ingestion | ✅ Done |
| **6** | OpenAPI — auto Swagger UI documentation | ✅ Done |

Updated on May 4th, 2026

---

## 🔧 Tech Stack

| Component | Tool |
|-----------|------|
| Language | Python 3.11+ |
| API Framework | FastAPI |
| ORM | SQLAlchemy 2 |
| Database | PostgreSQL 15 |
| Migrations | Alembic |
| Data source | [Celestrak](https://celestrak.org/) (TLE format) |
| ASGI Server | Uvicorn |

---

## 🚀 Installation

### Prerequisites

- Python 3.11+
- PostgreSQL 15+ (local or Docker)
- `pip` and `venv`

### 1. Clone the project

```bash
git clone https://github.com/your-username/tle-playground.git
cd tle-playground
```

### 2. Create and activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate       # Linux / macOS
# .\venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

```bash
cp .env.example .env
# Edit .env with your own values
```

`.env.example` content:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/tle_db
CELESTRAK_URL=https://celestrak.org/SOCRATES/query.php
```

### 5. Create the PostgreSQL database

```bash
psql -U postgres -c "CREATE DATABASE tle_db;"
```

### 6. Run migrations (Step 4+)

```bash
alembic upgrade head
```

---

## ▶️ Usage

### Run TLE ingestion

```bash
python ingest.py
```

### Start the API

```bash
uvicorn main:app --reload
```

API available at: [http://localhost:8000](http://localhost:8000)

### Available endpoints

| Method | Route | Description |
|--------|-------|-------------|
| `GET` | `/health` | Check the API is running |
| `GET` | `/satellites` | List all satellites in the database |
| `GET` | `/satellites/{id}` | Get a satellite by ID |

### Interactive documentation (Swagger UI)

```
http://localhost:8000/docs
```

---

## 📦 Main dependencies

```
fastapi
uvicorn[standard]
sqlalchemy>=2.0
psycopg2-binary
alembic
requests
python-dotenv
```

---

## 📡 TLE Format

A **TLE (Two-Line Element set)** is a NASA/NORAD standard format describing a satellite's orbit at a given point in time (the epoch).

```
ISS (ZARYA)
1 25544U 98067A   24001.50000000  .00001234  00000-0  12345-4 0  9999
2 25544  51.6400 208.9163 0006420  86.9953 273.1872 15.50377579123456
```

- **Line 0**: Satellite name
- **Line 1**: NORAD ID, epoch, orbital drag...
- **Line 2**: Inclination, RAAN, eccentricity, mean motion...

---

## 🤝 Contributing

Personal learning project — no external contributions planned for now.

---

## 📄 License

MIT

---

*Created as part of training for the Orekit website redesign project (2025–2026)*
