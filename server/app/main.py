# from fastapi import FastAPI, HTTPException, Body, Query, Path
# from pymongo import MongoClient
# from pydantic import BaseModel
# from typing import List, Optional
# from urllib.parse import quote_plus
# import os

# app = FastAPI()

# # MongoDB Connection Setup
# username = quote_plus('gocargo')
# password = quote_plus('Bluesky@2023')
# cluster = "cluster0.gatf1.mongodb.net"
# database_name = "mydatabase"
# client = MongoClient(
#     f"mongodb+srv://{username}:{password}@{cluster}/{database_name}?retryWrites=true&w=majority&appName=Cluster0"
# )
# db = client[database_name]
# users_collection = db["users"]
# cars_collection = db["cars"]

# # Models
# class UserAuth(BaseModel):
#     email: str
#     password: str

# class TokenResponse(BaseModel):
#     token: str
#     refreshToken: str
#     userId: str
#     expiresIn: int

# class UserRegistration(BaseModel):
#     email: str
#     password: str
#     username: str
#     phone: str

# class UserResponse(BaseModel):
#     userId: str
#     email: str
#     username: str

# class Car(BaseModel):
#     brand: str
#     model: str
#     year: str
#     type: Optional[str] = None
#     availability: str
#     driver_name: Optional[str] = None
#     driver_contact: Optional[str] = None

# class CarResponse(BaseModel):
#     id: str
#     brand: str
#     model: str
#     year: str
#     type: str
#     availability: str
#     driver_name: Optional[str] = None
#     driver_contact: Optional[str] = None

# # Auth Endpoints
# @app.post("/api/auth/login", response_model=TokenResponse)
# def login(auth_details: UserAuth):
#     # Assume a function to validate and create tokens
#     return {"token": "access_token", "refreshToken": "refresh_token", "userId": "user_id", "expiresIn": 3600}

# @app.post("/api/auth/register", response_model=UserResponse)
# def register(user: UserRegistration):
#     # Assume user registration logic
#     return {"userId": "user_id", "email": user.email, "username": user.username}

# @app.post("/api/auth/logout")
# def logout():
#     return {"message": "User logged out successfully"}

# @app.post("/api/auth/refresh", response_model=TokenResponse)
# def refresh_token(refresh_token: str = Body(...)):
#     # Assume token refresh logic
#     return {"token": "new_access_token", "refreshToken": "new_refresh_token", "expiresIn": 3600}

# # User Endpoints
# @app.get("/api/users/{userId}/cars", response_model=List[CarResponse])
# def get_user_cars(userId: str = Path(...)):
#     # Assume fetching user cars
#     return [{"id": "car_id", "brand": "Toyota", "model": "Camry", "year": "2021", "type": "Sedan", "availability": "Available"}]

# @app.get("/api/users/{userId}", response_model=UserResponse)
# def get_user(userId: str = Path(...)):
#     # Assume fetching user details
#     return {"userId": userId, "email": "example@example.com", "username": "userusername"}

# # Car Endpoints
# @app.post("/api/cars", response_model=CarResponse)
# def create_car(car: Car):
#     # Assume car creation logic that interacts with MongoDB
#     car_id = "generated_car_id"  # Placeholder for generated ID
#     car_dict = car.dict()
#     car_dict['id'] = car_id
#     # Save to database assumed here
#     return car_dict

# @app.get("/api/cars/{id}", response_model=CarResponse)
# def get_car(id: str):
#     # Fetch car from database using id
#     car_data = {
#         "id": id,
#         "brand": "Toyota",
#         "model": "Corolla",
#         "year": "2020",
#         "type": "Sedan",
#         "availability": "Available",
#         "driver_name": "John Doe",
#         "driver_contact": "123-456-7890"
#     }
#     return car_data
# @app.put("/api/cars/{id}", response_model=CarResponse)
# def update_car(id: str = Path(...), car: Car = Body(...)):
#     # Assume updating car details
#     return {"id": id, "brand": car.brand, "model": car.model, "year": car.year, "type": car.type, "availability": car.availability}

# @app.delete("/api/cars/{id}")
# def delete_car(id: str = Path(...)):
#     # Assume car deletion logic
#     return {"message": "Car deleted successfully"}

# server/app/main.py
from fastapi import FastAPI
from server.routers.auth import router as auth_router
from server.routers.users import router as user_router
from server.routers.cars import router as car_router

app = FastAPI()

# Include the routers with the appropriate prefixes
app.include_router(auth_router, prefix="/api/auth")
app.include_router(user_router, prefix="/api/users")
app.include_router(car_router, prefix="/api/cars")
# You can include other routers here as needed