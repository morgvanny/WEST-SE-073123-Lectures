#!/usr/bin/env python3

# 📚 Review With Students:
# Request-Response Cycle
# Web Servers and WSGI/Werkzeug

# 1. ✅ Navigate to `models.py`

# 2. ✅ Set Up Imports


# 3. ✅ Initialize the App


# Configure the database
# ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'`
# ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False`


# 4. ✅ Migrate

# 5. ✅ Navigate to `seed.rb`

# 6. ✅ Routes


# 7. ✅ Run the server with `flask run` and verify your route in the browser at `http://localhost:5000/`

# 8. ✅ Create a dynamic route


# 9.✅ Update the route to find a `production` by its `title` and send it to our browser


# Note: If you'd like to run the application as a script instead of using `flask run`, uncomment the line below
# and run `python app.py`

# if __name__ == '__main__':
#     app.run(port=5000, debug=True)


from flask import Flask, make_response
from flask_migrate import Migrate
from models import Production, db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route("/productions")
def productions():
    prods = Production.query.all()
    return make_response([p.to_dict() for p in prods], 200)


@app.route("/productions/<int:id>")
def production_by_id(id):
    prod = Production.query.get(id)
    if prod:
        return make_response(prod.to_dict(), 200)
    else:
        return make_response({"error": "Production not found."}, 404)


if __name__ == "__main__":
    app.run(port=5555, debug=True)
