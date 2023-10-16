from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()


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
