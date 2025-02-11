from pydantic import BaseModel, EmailStr

class UserAuth(BaseModel):
    email: str
    password: str

class TokenResponse(BaseModel):
    token: str
    refreshToken: str
    userId: str
    expiresIn: int

class UserRegistration(BaseModel):
    email: str
    password: str
    username: str
    phone: str

