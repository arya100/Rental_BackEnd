# server/routers/car.py

from pydantic import BaseModel
from typing import Optional

class Car(BaseModel):
    brand: str
    model: str
    year: str
    type: Optional[str] = None
    availability: str
    driver_name: Optional[str] = None
    driver_contact: Optional[str] = None

class CarResponse(BaseModel):
    id: str
    brand: str
    model: str
    year: str
    type: str
    availability: str
    driver_name: Optional[str] = None
    driver_contact: Optional[str] = None

