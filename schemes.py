from pydantic import BaseModel, EmailStr

class UserSignup(BaseModel):
    name: str
    phone: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    phone_or_email: str
    password: str
