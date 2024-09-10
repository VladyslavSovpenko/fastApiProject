from typing import List, Optional

from pydantic import EmailStr, BaseModel
from sqlalchemy import Column, ForeignKey, JSON
from sqlmodel import SQLModel, Field, Relationship


class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    creator: Optional[str]
    title: str
    image: str
    description: str
    location: str
    tags: List[str] = Field(sa_column=Column(JSON))

    # Foreign key linking to User
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")

    user: Optional["User"] = Relationship(back_populates="events")

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


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: EmailStr
    password: str
    events: Optional[List[Event]] = Relationship(back_populates="user")

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
                "events": [],
            }
        }
class TokenResponse(BaseModel):
    access_token: str
    token_type: str