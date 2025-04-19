import requests
import os 
from dotenv import load_dotenv

load_dotenv()

class AnimalPictures: 
    @classmethod
    def generate_animal(cls, animal_type: str) -> dict:
        match animal_type.upper():
            case "CAT":
                return cls.get_cats(1)[0]
            case "DOG":
                return cls.get_dogs(1)[0]
            case _:
                raise ValueError("Invalid animal type")

    @classmethod
    def get_cats(cls, limit: int = 1) -> dict:
        url: str = "https://api.thecatapi.com/v1/images/search?limit=%s" % limit
        print("URL: ", url)
        print("API KEY: ", os.getenv("DOG_CAT_API_KEY"))
        headers: dict = {
            'x-api-key': os.getenv("DOG_CAT_API_KEY"),
            'Content-Type': 'application/json'
        }
        response: dict = requests.get(url, headers=headers).json()
        return response

    @classmethod
    def get_dogs(cls, limit: int = 1) -> dict: 
        url: str = "https://api.thedogapi.com/v1/images/search?limit=%s" % limit
        headers: dict = {
            'x-api-key': os.getenv("DOG_CAT_API_KEY"),
            'Content-Type': 'application/json'
        }
        response: dict = requests.get(url, headers=headers).json()
        return response





