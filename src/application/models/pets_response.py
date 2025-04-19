import pydantic
from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from .animal_record import AnimalRecord

class PetsResponse(BaseModel):
    requested_animal_type: str
    status: str = "success"
    error: Optional[str] = None
    timestamp: datetime = datetime.now()
    pet_count: int = 0
    pets: list[AnimalRecord]