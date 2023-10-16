from os import environ

from cast_member_resources import CastMemberResource, CastMembersResource
from dotenv import load_dotenv
from flask import Flask, make_response, request, session
from flask_migrate import Migrate
from flask_restful import Api
from models import Production, db

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
migrate = Migrate(app, db)
db.init_app(app)
load_dotenv(".env")
app.secret_key = environ.get("SECRET_KEY")


@app.route("/set_user", methods=["GET"])
def set_user():
    # find the user from username
    # check if password is valid
    # if so, set user_id to that user's id
    session["user_id"] = 2
    return make_response("signed in as user # 2", 200)


@app.route("/me", methods=["GET"])
def me():
    return make_response("user # " + request.cookies.get("user_id"), 200)


@app.route("/set_red", methods=["GET"])
def set_red():
    res = make_response("setting cookie to red", 200)
    res.set_cookie("color", value="red")
    return res


@app.route("/set_blue", methods=["GET"])
def set_blue():
    res = make_response("setting cookie to blue", 200)
    res.set_cookie("color", value="blue")
    return res


@app.route("/set_green", methods=["GET"])
def set_green():
    res = make_response("setting cookie to green", 200)
    res.set_cookie("color", value="green")
    return res


@app.route("/cookie_color", methods=["GET"])
def cookie_color():
    return make_response(request.cookies.get("color"), 200)


@app.route("/productions", methods=["GET"])
def productions():
    prods = Production.query.all()
    return make_response([p.to_dict() for p in prods], 200)


@app.route("/productions", methods=["POST"])
def create_production():
    production_json = request.get_json()
    try:
        properties = [
            "title",
            "image",
            "ongoing",
            "genre",
            "director",
            "description",
            "budget",
        ]
        production = Production()
        for prop in properties:
            setattr(production, prop, production_json.get(prop))
        db.session.add(production)
        db.session.commit()
        return make_response(production.to_dict(), 201)
    except ValueError as e:
        return make_response({"error": e.__str__()}, 422)


@app.route("/productions/<int:id>", methods=["GET", "PATCH", "DELETE"])
def production_by_id(id):
    prod = Production.query.get(id)
    if not prod:
        return make_response({"message": "Production not found."}, 404)
    if request.method == "GET":
        return make_response(prod.to_dict(), 200)
    elif request.method == "PATCH":
        data = request.get_json()
        try:
            for attr in data:
                setattr(prod, attr, data.get(attr))
            db.session.commit()
            return make_response(prod.to_dict(), 200)
        except ValueError as e:
            return make_response({"error": e.__str__()})
    elif request.method == "DELETE":
        db.session.delete(prod)
        db.session.commit()
        return "", 204


api.add_resource(CastMemberResource, "/castmembers/<int:id>")
api.add_resource(CastMembersResource, "/castmembers")

if __name__ == "__main__":
    app.run(port=5555, debug=True)
