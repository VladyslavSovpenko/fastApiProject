from fastapi import APIRouter, HTTPException

from models.models import NewUser, UserSignIn

user_router = APIRouter(tags=['User'])

users = {}


@user_router.post("/signup")
def signup(request: NewUser):
    if request.email in users:
        raise HTTPException(status_code=409, detail="Email already registered")
    users[request.email] = request
    return {"message": "Email registered"}


@user_router.post("/signin")
def user_sign_in(request: UserSignIn):
    if request.email not in users:
        raise HTTPException(status_code=404, detail="Email not found")
    if users[request.email].password != request.password:
        raise HTTPException(status_code=403, detail="Password mismatch")
    return {"message": "User signed in"}
