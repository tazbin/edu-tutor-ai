# Edu Tutor AI

FastAPI backend.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Database

Postgres 17 with pgvector, via Docker Compose:

```bash
docker compose up -d     # start
docker compose down      # stop (data kept in the edututor_ai_pgdata volume)
```

Defaults: user/password/db `edututor_ai` on port `5432`. Override with `POSTGRES_USER`,
`POSTGRES_PASSWORD`, `POSTGRES_DB`, `POSTGRES_PORT` in a `.env` file. SQL files in `db/init/`
run once, on first start with an empty volume.

## Run

```bash
fastapi dev app/main.py
```

- Health check: http://127.0.0.1:8000/health
- API docs: http://127.0.0.1:8000/docs
