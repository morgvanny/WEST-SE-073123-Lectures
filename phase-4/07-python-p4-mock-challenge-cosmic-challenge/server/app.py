#!/usr/bin/env python3

import os

from flask import Flask, make_response, request
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import Mission, Planet, Scientist, db

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False
migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)


@app.route("/")
def home():
    return ""


class Scientists(Resource):
    def get(self):
        return make_response(
            [scientist.to_dict() for scientist in Scientist.query.all()], 200
        )

    def post(self):
        scientist_json = request.get_json()
        scientist = Scientist()

        try:
            for key in scientist_json:
                if hasattr(scientist, key):
                    setattr(scientist, key, scientist_json[key])
            db.session.add(scientist)
            db.session.commit()
            return make_response(scientist.to_dict(), 201)
        except ValueError:
            return make_response({"errors": ["validation errors"]}, 400)


class ScientistById(Resource):
    def get(self, id):
        scientist = db.session.get(Scientist, id)  # Scientist.query.get(id)
        if scientist:
            return make_response(scientist.to_dict(rules=("missions",)), 200)

        return make_response({"error": "Scientist not found"}, 404)

    def patch(self, id):
        scientist = db.session.get(Scientist, id)

        if scientist:
            scientist_json = request.get_json()
            try:
                for key in scientist_json:
                    if hasattr(scientist, key):
                        setattr(scientist, key, scientist_json[key])
                db.session.commit()
                return make_response(scientist.to_dict(), 202)
            except ValueError:
                return make_response({"errors": ["validation errors"]}, 400)

        return make_response({"error": "Scientist not found"}, 404)

    def delete(self, id):
        scientist = db.session.get(Scientist, id)

        if scientist:
            db.session.delete(scientist)
            db.session.commit()
            return "", 204

        return make_response({"error": "Scientist not found"}, 404)


class Planets(Resource):
    def get(self):
        return make_response([planet.to_dict() for planet in Planet.query.all()], 200)


class Missions(Resource):
    def post(self):
        mission_json = request.get_json()
        mission = Mission()
        try:
            for key in mission_json:
                if hasattr(mission, key):
                    setattr(mission, key, mission_json[key])
            db.session.add(mission)
            db.session.commit()
            return make_response(mission.to_dict(rules=("scientist",)), 201)
        except ValueError:
            return make_response({"errors": ["validation errors"]}, 400)


api.add_resource(Missions, "/missions")
api.add_resource(Scientists, "/scientists")
api.add_resource(ScientistById, "/scientists/<int:id>")
api.add_resource(Planets, "/planets")

if __name__ == "__main__":
    app.run(port=5555, debug=True)
