from typing import List, Optional

from pydantic import BaseModel, EmailStr


class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
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
