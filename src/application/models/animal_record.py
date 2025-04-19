from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class Animals(Enum):
    CAT = 1
    DOG = 2

    @classmethod
    def check_animal_exist(cls, animal_type: str) -> str:
        try:
            return cls[animal_type].value
        except KeyError:
            return None

class AnimalRecord(BaseModel):
    petId: str
    name: str
    animalTypeId: int
    width: int
    height: int
    created_at: datetime = datetime.now()
    url: str
    animal_type: str

        