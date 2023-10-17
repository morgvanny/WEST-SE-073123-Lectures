from cast_member_resources import CastMemberResource, CastMembersResource
from config import api, app
from flask import make_response, request, session
from models import Production, User, db
from sqlalchemy.exc import IntegrityError


@app.route("/set_user", methods=["GET"])
def set_user():
    # find the user from username
    # check if password is valid
    # if so, set user_id to that user's id
    session["user_id"] = 2
    return make_response("signed in as user # 2", 200)


@app.route("/signup", methods=["POST"])
def signup():
    user_json = request.get_json()
    user = User()
    try:
        for key in user_json:
            if hasattr(user, key):
                setattr(user, key, user_json[key])
        user.password_hash = user_json.get("password")
        db.session.add(user)
        db.session.commit()
        session["user_id"] = user.id
        return make_response(user.to_dict(), 201)
    except ValueError as e:
        return make_response({"error": e.__str__()}, 422)
    except IntegrityError:
        return make_response({"error": "Username must be unique"}, 422)


@app.route("/login", methods=["POST"])
def login():
    user_json = request.get_json()
    user = User.query.filter(User.username == user_json.get("username"))[0]
    if user and user.authenticate(user_json.get("password")):
        session["user_id"] = user.id
        return make_response(user.to_dict(), 200)
    else:
        return make_response({"error": "Username or password is incorrect"}, 401)


@app.route("/me", methods=["GET"])
def me():
    user = db.session.get(User, session.get("user_id"))
    if user:
        return make_response(user.to_dict(), 200)
    else:
        return make_response({"error": "not logged in"}, 401)


@app.route("/logout", methods=["DELETE"])
def logout():
    session.clear()
    return make_response("", 204)


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
    if not find_user():
        return make_response({"error": "user must log in first"}, 401)
    prods = Production.query.all()
    return make_response([p.to_dict() for p in prods], 200)


@app.route("/productions", methods=["POST"])
def create_production():
    if not find_user():
        return make_response({"error": "user must log in first"}, 401)
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
    if not find_user():
        return make_response({"error": "user must log in first"}, 401)
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


def find_user():
    return db.session.get(User, session.get("user_id"))


api.add_resource(CastMemberResource, "/castmembers/<int:id>")
api.add_resource(CastMembersResource, "/castmembers")

if __name__ == "__main__":
    app.run(port=5555, debug=True)
