from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import select
from fastapi.security import OAuth2PasswordRequestForm

from auth.hash_password import HashPassword
from auth.jwt_handler import create_access_token
from database.connection import get_session
from models.models import User, TokenResponse

user_router = APIRouter(tags=['User'])
hash_password = HashPassword()


@user_router.post("/signup")
def signup(user: User, session=Depends(get_session)) -> dict:
    if session.exec(select(User).where(User.email == user.email)).first():
        raise HTTPException(status_code=409, detail="Email already registered")
    hashed_user_password = hash_password.create_hash(user.password)
    user.password = hashed_user_password

    session.add(user)
    session.commit()
    session.refresh(user)
    return {"message": "Email registered"}


@user_router.post("/signin", response_model=TokenResponse)
def user_sign_in(user: OAuth2PasswordRequestForm = Depends(), session=Depends(get_session)) -> dict:
    user_exist = session.exec(select(User).where(User.email == user.username)).first()
    if user_exist:
        if hash_password.verify_hash(user.password, user_exist.password):
            access_token = create_access_token(user_exist.email)
            return {
                "access_token": access_token,
                "token_type": "Bearer"
            }
