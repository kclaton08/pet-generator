from flask import Blueprint, request, jsonify
from flask import Response
from db import db
from models.animal_record import Animals, AnimalRecord
from middleware.animal_pictures import AnimalPictures
from models.pets_response import PetsResponse
from datetime import datetime
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

repsository_blueprint = Blueprint("repsository_blueprint", __name__, url_prefix="/pet-repository")

@repsository_blueprint.route("/", methods=["GET"])
def get_pets() -> Response:
    animal_type = request.args.get("animal_type", default=None)
    animalId: int = Animals.check_animal_exist(animal_type.upper()) if animal_type is not None else None
    if animalId == 0: 
        response: PetsResponse = PetsResponse(
            status="error",
            timestamp=datetime.now(),
            pets=[],
            error=f"{animal_type} is not a valid animal type. Please use either 'cat' or 'dog'."
        )
        return jsonify(response.model_dump()), 500
    try: 
        if animalId is None:
            result: list[dict] = db.find_data({}, limit=request.args.get("limit", 1))
        else:
            result: list[dict] = db.find_data({"animalId": animalId}, limit=request.args.get("limit", 1))
        if result:
            pets: list[AnimalRecord] = []
            for record in result: 
                pets.append(AnimalRecord(
                    petId=str(record["_id"]),
                    name=record["name"],
                    animalTypeId=record["animalId"],
                    width=record["width"],
                    height=record["height"],
                    created_at=record["created_at"],
                    url=record["url"],
                    animal_type=record["animal_type"],
                ))
            response: PetsResponse = PetsResponse(
                timestamp=datetime.now(),
                status="success",
                pet_count=len(pets),
                pets=[record.model_dump() for record in pets]
            )

            return jsonify(response.model_dump()), 200
        else:
            response: PetsResponse = PetsResponse(
                status="error",
                timestamp=datetime.now(),
                pets=[],
                error=f"animal type: {animal_type} has no records."
            )
            return jsonify(response.model_dump()), 404
    except Exception as e:
        logger.error(f"The following error occured when processing the request: {e}")
        response: PetsResponse = PetsResponse(
            status="error",
            timestamp=datetime.now(),
            pets=[],
            error=f"An error occured while fetching your pets! Please try again."
        )
        return jsonify(response.model_dump()), 500

        