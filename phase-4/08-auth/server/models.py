# 📚 Review With Students:
# Review models
# Review MVC
# SQLAlchemy import
import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

# 📚 Review With Students:
# What SQLAlchemy() is replacing from SQLAlchemy in phase 3

db = SQLAlchemy()
# 1. ✅ Create a Production Model
# tablename = 'Productions'
# Columns:
# title: string, genre: string, budget:float, image:string,director: string,
# description:string, ongoing:boolean, created_at:date time, updated_at: date time
# 2. ✅ navigate to app.py


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
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow
    )

    cast_members = db.relationship(
        "CastMember", backref="production", lazy=True, cascade="all,delete-orphan"
    )

    serialize_rules = (
        "-created_at",
        "-updated_at",
        "-cast_members.production",
        "-cast_members.production_id",
        "-cast_members.id",
    )

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
        if isinstance(image, str) and image[len(image) - 5 :] != ".jpeg":
            raise ValueError("Image must be a .jpeg")
        return image

    @validates("ongoing")
    def validate_ongoing(self, key, ongoing):
        if ongoing is not None and not isinstance(ongoing, bool):
            raise ValueError("Ongoing attribute must be a boolean.")
        return ongoing

    # @validates("title")
    # def validate_title_uniqueness(self, key, title):
    #     import ipdb

    #     ipdb.set_trace()
    #     titles = [production.title for production in type(self).query.all()]
    #     if title in titles:
    #         raise ValueError("Title must be unique")
    #     return title


class CastMember(db.Model, SerializerMixin):
    __tablename__ = "cast_members"

    serialize_rules = ("-production.cast_members",)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    production_id = db.Column(
        db.Integer, db.ForeignKey("productions.id"), nullable=False
    )

    @validates("name")
    def validate_name(self, key, name):
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string.")
        return name


class Appointment(db.Model):
    __tablename__ = "appointments"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey("doctors.id"), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey("patients.id"), nullable=False)
    doctor = db.relationship("Doctor", back_populates="appointments")
    patient = db.relationship("Patient", back_populates="appointments")


class Doctor(db.Model):
    __tablename__ = "doctors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialty = db.Column(db.String(100), nullable=False)

    appointments = db.relationship(
        "Appointment", back_populates="doctor", lazy=True, cascade="all,delete-orphan"
    )

    patients = association_proxy("appointments", "patient")


class Patient(db.Model):
    __tablename__ = "patients"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    appointments = db.relationship(
        "Appointment", back_populates="patient", lazy=True, cascade="all,delete-orphan"
    )

    doctors = association_proxy("appointments", "doctor")


# CRUD

# index (list of records)
# show (single record)
# create (make new record)
# update (update record)
# destroy (delete record)


# index (list of records) GET
# show (single record) GET
# create (make new record) POST
# new (form to make new record) GET
# update (update record) PATCH
# edit (form to edit a record) GET
# destroy (delete record) DELETE
# button somewhere on a page was received by GET

# GET /productions - get an index (list) of productions
# POST /productions - send data to make a new production

# GET /productions/<int:id> - get a single production
# PATCH/PUT /productions/<int:id> - update a single production
# DELETE /productions/<int:id> - destroy a single production
