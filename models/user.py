from pydantic import BaseModel, EmailStr

class UserResponse(BaseModel):
    userId: str
    email: str
    username: str
