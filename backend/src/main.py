from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .common.db import create_db_and_tables, SessionDep
from .routers import main, user

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(main.router)
app.include_router(user.router)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    user.create_admin_user()