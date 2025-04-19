import os 
from flask import Flask
from dotenv import load_dotenv
from routes.pet_generator import frontend_blueprint
from routes.pet_repository import repsository_blueprint

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False

app.register_blueprint(frontend_blueprint)
app.register_blueprint(repsository_blueprint)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)


