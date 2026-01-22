from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from vectorstore.qdrant_store import save_user, verify_user

router = APIRouter()

class UserSignup(BaseModel):
    name: str
    phone: str
    email: str
    password: str

class UserLogin(BaseModel):
    phone_or_email: str
    password: str

@router.post("/signup")
def signup(user: UserSignup):
    if not all([user.name, user.phone, user.email, user.password]):
        raise HTTPException(status_code=422, detail="All fields required")
    save_user(user.dict())
    return {"message": "User registered successfully"}

@router.post("/login")
def login(user: UserLogin):
    if not all([user.phone_or_email, user.password]):
        raise HTTPException(status_code=422, detail="All fields required")
    if verify_user(user.phone_or_email, user.password):
        return {"message": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
