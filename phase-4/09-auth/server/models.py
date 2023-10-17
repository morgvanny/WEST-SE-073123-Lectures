from config import bcrypt, db
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin


class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)
    _password_hash = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    serialize_rules = ("-_password_hash", "-created_at", "-updated_at")

    @hybrid_property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, password):
        # utf-8 encoding and decoding is required in python 3
        password_hash = bcrypt.generate_password_hash(password.encode("utf-8"))
        self._password_hash = password_hash.decode("utf-8")

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode("utf-8"))


class Production(db.Model, SerializerMixin):
    __tablename__ = "productions"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True)
    genre = db.Column(db.String)
    budget = db.Column(db.Float)
    image = db.Column(db.String)
    director = db.Column(db.String)
    description = db.Column(db.String)
    ongoing = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    cast_members = db.relationship(
        "CastMember",
        back_populates="production",
        lazy=True,
        cascade="all,delete-orphan",
    )

    serialize_rules = ("-cast_members.production",)

    @validates("title")
    def validate_title(self, key, title):
        if not title:
            raise ValueError("Productions must have a title.")
        if len(title) > 100:
            raise ValueError("Title must be 100 characters or less.")
        if type(self).query.filter_by(title=title).first():
            raise ValueError("Title must be unique.")
        return title

    @validates("image")
    def validate_image(self, key, image):
        if image and not isinstance(image, str):
            raise ValueError("Image must be a string, or left blank.")
        if isinstance(image, str) and image[len(image) - 4 :] != ".jpg":
            raise ValueError("Image must be a .jpg")
        return image

    @validates("ongoing")
    def validate_ongoing(self, key, ongoing):
        if ongoing is not None and not isinstance(ongoing, bool):
            raise ValueError("Ongoing attribute must be a boolean.")
        return ongoing


class CastMember(db.Model, SerializerMixin):
    __tablename__ = "cast_members"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    role = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    production_id = db.Column(
        db.Integer, db.ForeignKey("productions.id"), nullable=False
    )

    production = db.relationship("Production", back_populates="cast_members")

    serialize_rules = ("-production.cast_members",)

    @validates("name")
    def validate_name(self, key, name):
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string.")
        return name
