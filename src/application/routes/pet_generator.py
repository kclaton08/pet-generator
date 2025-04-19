from flask import Blueprint
from flask import render_template, request, session, redirect, url_for
from flask import Response
from db import db
from models.animal_record import Animals
from middleware.animal_pictures import AnimalPictures
from datetime import datetime

frontend_blueprint = Blueprint("frontend_blueprint", __name__, url_prefix="/pet-generator")

@frontend_blueprint.route("/", methods=["GET"])
def view_pet_generator() -> Response:
    data: dict = {
        "show_image": False
    }
    return render_template('petGenerator.html', data=data)

@frontend_blueprint.route("/generate", methods=["POST"])
def generate_pet() -> Response:
    animal_type = request.form.get('animal_type')
    animalId: int = Animals.check_animal_exist(animal_type.upper())
    try:
        response = AnimalPictures.generate_animal(animal_type)
        data = {
            "animalId": animalId,
            "name": request.form.get('pet_name'),
            "width": response.get("width"),
            "height": response.get("height"),
            "url": response.get("url"),
            "animal_type": animal_type.upper(),
            "created_at": datetime.now()
        }
        db.insert_data(data)
        data.update({
            "show_image": True,
        })
        return render_template('petGenerator.html', data=data)
    except Exception as e:
        session['error_message'] = f'There was an error generating your pet! Please try again.'
        return redirect(url_for('frontend_blueprint.error'))

@frontend_blueprint.route("/view", methods=["GET"])
def view_pets() -> Response:
    data = db.find_data({"animalId": {"$in": [Animals.CAT.value, Animals.DOG.value]}}, limit=1000)
    for record in data:
        record['created_at'] = record['created_at'].strftime("%Y-%m-%d %H:%M:%S")
    return render_template('viewPets.html', data=data)

@frontend_blueprint.route("/error", methods=["GET"])
def error() -> Response:
    data: dict = {
        "error_message": session.get('error_message', None)
    }
    return render_template('error.html', data=data)



