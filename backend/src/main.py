from fastapi import FastAPI

from .common.db import create_db_and_tables, SessionDep
from .routers import main, user

app = FastAPI()

app.include_router(main.router)
app.include_router(user.router)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    user.create_admin_user()