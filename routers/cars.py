from fastapi import APIRouter, Body, Path
from models.car import  Car, CarResponse
from typing import Optional

router = APIRouter()

@router.post("/", response_model=CarResponse)
def create_car(car: Car):
    # Assume car creation logic that interacts with MongoDB
    car_id = "generated_car_id"  # Placeholder for generated ID
    car_dict = car.dict()
    car_dict['id'] = car_id
    # Save to database assumed here
    return car_dict

@router.get("/{id}", response_model=CarResponse)
def get_car(id: str):
    # Fetch car from database using id
    car_data = {
        "id": id,
        "brand": "Toyota",
        "model": "Corolla",
        "year": "2020",
        "type": "Sedan",
        "availability": "Available",
        "driver_name": "John Doe",
        "driver_contact": "123-456-7890"
    }
    return car_data

@router.put("/{id}", response_model=CarResponse)
def update_car(id: str = Path(...), car: Car = Body(...)):
    # Assume updating car details
    return {"id": id, "brand": car.brand, "model": car.model, "year": car.year, "type": car.type, "availability": car.availability}

@router.delete("/{id}")
def delete_car(id: str = Path(...)):
    # Assume car deletion logic
    return {"message": "Car deleted successfully"}