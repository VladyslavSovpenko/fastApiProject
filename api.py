from fastapi import FastAPI

from database.connection import conn
from routes.events import event_router
from routes.users import user_router
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await conn()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")
