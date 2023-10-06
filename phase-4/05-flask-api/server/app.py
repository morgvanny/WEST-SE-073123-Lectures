from cast_member_resources import CastMemberResource, CastMembersResource
from flask import Flask, make_response, request
from flask_migrate import Migrate
from flask_restful import Api
from models import Production, db

app = Flask(__name__)

api = Api(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route("/productions", methods=["GET"])
def productions():
    prods = Production.query.all()
    return make_response([p.to_dict() for p in prods], 200)


@app.route("/productions", methods=["POST"])
def create_production():
    production_json = request.get_json()

    try:
        production = Production(
            title=production_json["title"], image=production_json["image"]
        )
        db.session.add(production)
        db.session.commit()

        return make_response(production.to_dict(), 201)
    except ValueError as e:
        return make_response({"error": e.__str__()})


@app.route("/productions/<int:id>", methods=["GET", "PATCH", "DELETE"])
def production_by_id(id):
    prod = Production.query.get(id)
    if not prod:
        return make_response({"message": "Production not found."}, 404)
        # abort(404, "Production not found.")
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
    app.run(port=5555, debug=True)
