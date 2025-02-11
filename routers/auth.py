from fastapi import APIRouter, Body
from models.Auth import UserAuth,  TokenResponse, UserRegistration
from models.user import UserResponse

router = APIRouter()

@router.post("/login", response_model=TokenResponse)
def login(auth_details: UserAuth):
    # Logic for logging in the user
    return {"token": "access_token", "refreshToken": "refresh_token", "userId": "user_id", "expiresIn": 3600}

@router.post("/register", response_model=UserResponse )
def register(user: UserRegistration):
    # Logic for registering a new user
    return {"userId": "user_id", "email": user.email, "username": user.username}

@router.post("/logout")
def logout():
    # Logic for logging out the user
    return {"message": "User  logged out successfully"}

@router.post("/refresh", response_model=TokenResponse)
def refresh_token(refresh_token: str = Body(...)):
    # Logic for refreshing the token
    return {"token": "new_access_token", "refreshToken": "new_refresh_token", "expiresIn": 3600}