# server/routers/user.py
from fastapi import APIRouter, Path
from models.user import UserResponse
from models.car import CarResponse
from typing import List
from config.database import users_collection
from bson import ObjectId



router = APIRouter()
@router.get("/")
def get_users():
    # Assume fetching user details
    users=users_collection.find()
    _users=[]
    for user in users:
        user["id"]=str(user["_id"])
        del user["_id"]
        _users.append(user)

    return _users

@router.get("/{userId}")
def get_user(userId: str = Path(...)):
    # Assume fetching user details
    user=users_collection.find_one({"_id":ObjectId(userId)})
    user["id"]=str(user["_id"])
    del user["_id"]
    

    return user

@router.post("")
def create_user(response_model:UserResponse):
    # Assume fetching user details
    users_collection.insert_one(dict(response_model))
    return "Added"

@router.get("/{userId}/cars", response_model=List[CarResponse])
def get_user_cars(userId: str = Path(...)):
    # Assume fetching user cars
    return [{"id": "car_id", "brand": "Toyota", "model": "Camry", "year": "2021", "type": "Sedan", "availability": "Available"}]