from fastapi import FastAPI

from .common.db import create_db_and_tables
from .routers import main

app = FastAPI()

app.include_router(main.router)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()