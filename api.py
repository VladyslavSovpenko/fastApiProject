from fastapi import FastAPI

from database.connection import conn
from routes.events import event_router
from routes.users import user_router

app = FastAPI()
app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")


@app.on_event("startup")
async def on_startup():
    conn()
