#!/usr/bin/env python3

import os

from flask import Flask, make_response, request
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import Activity, Camper, Signup, db

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


class Campers(Resource):
    def get(self):
        campers = Camper.query.all()

        return make_response(
            [camper.to_dict(rules=("-signups",)) for camper in campers], 200
        )

    def post(self):
        camper_json = request.get_json()
        camper = Camper()

        try:
            for key in camper_json:
                if hasattr(camper, key):
                    setattr(camper, key, camper_json[key])
            db.session.add(camper)
            db.session.commit()
            return make_response(camper.to_dict(rules=("-signups",)), 201)
        except ValueError:
            return make_response({"errors": ["validation errors"]}, 400)


class CamperById(Resource):
    def get(self, id):
        camper = Camper.query.get(id)
        if camper:
            return make_response(camper.to_dict(), 200)
        else:
            return make_response({"error": "Camper not found"}, 404)

    def patch(self, id):
        camper_json = request.get_json()
        camper = Camper.query.get(id)
        if camper:
            try:
                for key in camper_json:
                    if hasattr(camper, key):
                        setattr(camper, key, camper_json[key])
                db.session.commit()

                return make_response(camper.to_dict(rules=("-signups",)), 202)
            except ValueError:
                return make_response({"errors": ["validation errors"]}, 400)
        else:
            return make_response({"error": "Camper not found"}, 404)


api.add_resource(Campers, "/campers")
api.add_resource(CamperById, "/campers/<int:id>")


class Activities(Resource):
    def get(self):
        activities = Activity.query.all()

        return make_response(
            [activity.to_dict(rules=("-signups",)) for activity in activities], 200
        )


class ActivityById(Resource):
    def delete(self, id):
        activity = Activity.query.get(id)

        if activity:
            db.session.delete(activity)
            db.session.commit()
            return make_response("", 204)
        else:
            return make_response({"error": "Activity not found"}, 404)


api.add_resource(Activities, "/activities")
api.add_resource(ActivityById, "/activities/<int:id>")


class Signups(Resource):
    def post(self):
        signup_json = request.get_json()
        signup = Signup()

        try:
            for key in signup_json:
                if hasattr(signup, key):
                    setattr(signup, key, signup_json[key])
            db.session.add(signup)
            db.session.commit()
            return make_response(signup.to_dict(), 201)
        except ValueError:
            return make_response({"errors": ["validation errors"]}, 400)


api.add_resource(Signups, "/signups")

if __name__ == "__main__":
    app.run(port=5555, debug=True)
