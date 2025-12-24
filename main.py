from fastapi import FastAPI
from src.api.router import router

app = FastAPI(
    title="Bohra Prayer Engine",
    version="1.0",
    description="API for calculating Bohra prayer times"
)

app.include_router(router, prefix="/api")
