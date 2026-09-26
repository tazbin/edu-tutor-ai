from fastapi import FastAPI

from app.api.routes import health

app = FastAPI(title="Edu Tutor AI", version="0.1.0")

app.include_router(health.router)
