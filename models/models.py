from typing import List, Optional

from pydantic import BaseModel, EmailStr
from sqlalchemy import Column, JSON
from sqlmodel import SQLModel, Field


class Event(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    location: str
    tags: List[str] = Field(sa_column=Column(JSON))

    class Config:
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }


class User(BaseModel):
    email: EmailStr
    password: str
    events: Optional[List[Event]]

    class Config:
        json_schema_extra = {
            "email": "fastapi@packt.com",
            "username": "strong!!!",
            "events": [],

        }


class EventUpdate(SQLModel):
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]

    class Config:
        json_schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet",
                "description": "We will be discussing the contents of the FastAPI book in this event",
            }
        }


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "email": "fastapi@packt.com",
            "password": "<PASSWORD>",
        }
        # class TodoItem(BaseModel):
        #     item: str
        #
        #     class Config:
        #         json_schema_extra = {
        #             "example": {
        #                 "item": "Read the next chapter of the book"
        #             }
        #         }
        #
        # class TodoItems(BaseModel):
        #     todos: List[TodoItem]
        #
        #     class Config:
        #         json_schema_extra = {
        #             "example": {
        #                 "todos": [
        #                     {
        #                         "item": "Example schema 1!"
        #                     },
        #                     {
        #                         "item": "Example schema 2!"
        #                     }
        #                 ]}}


class NewUser(UserSignIn):
    pass
