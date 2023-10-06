#!/usr/bin/env python3
# 📚 Review With Students:
# Seeding
# 5. ✅ Imports
from datetime import datetime

from app import app
from models import Appointment, CastMember, Doctor, Patient, Production, db

# db and Production from models

# 6. ✅ Initialize the SQLAlchemy instance with `db.init_app(app)`


# 7. ✅ Create application context `with app.app_context():`
# Info on application context: https://flask.palletsprojects.com/en/1.1.x/appcontext/

with app.app_context():
    Production.query.delete()
    productions_to_delete = Production.query.all()
    for production in productions_to_delete:
        db.session.delete(production)

    doctors_to_delete = Doctor.query.all()
    for doctor in doctors_to_delete:
        db.session.delete(doctor)

    patients_to_delete = Patient.query.all()
    for patient in patients_to_delete:
        db.session.delete(patient)

    db.session.commit()

    try:
        p1 = Production(
            title="Hamlet",
            genre="Drama",
            director="Bill Shakespeare",
            description="The Tragedy of Hamlet, Prince of Denmark",
            budget=100000.00,
            image="https://upload.wikimedia.org/wikipedia/commons/6/6a/Edwin_Booth_Hamlet_1870.jpeg",
            ongoing=True,
        )

        db.session.add(p1)
    except ValueError as e:
        print(e.__str__())

    p2 = Production(
        title="Cats",
        genre="Musical",
        director="Andrew Lloyd Webber",
        description=" Jellicles cats sing and dance",
        budget=200000.00,
        image="https://upload.wikimedia.org/wikipedia/en/3/3e/CatsMusicalLogo.jpeg",
        ongoing=True,
    )

    db.session.add(p2)

    p3 = Production(
        title="Carmen",
        genre="Opera",
        director="Georges Bizet",
        description="Set in southern Spain this is the story of the downfall of Don"
        "José, a naïve soldier who is seduced by the wiles of the fiery and beautiful"
        "Carmen.",
        budget=200000.00,
        image="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Prudent-Louis_Leray_-_Poster_for_the_premi%C3%A8re_of_Georges_Bizet%27s_Carmen.jpg/300px-Prudent-Louis_Leray_-_Poster_for_the_premi%C3%A8re_of_Georges_Bizet%27s_Carmen.jpeg",
        ongoing=False,
    )

    db.session.add(p3)
    p4 = Production(
        title="Hamilton",
        genre="Musical",
        director="Lin-Manuel Miranda",
        description="An American Musical is a sung-and-rapped-through musical by "
        "Lin-Manuel Miranda. It tells the story of American Founding Father Alexander "
        "Hamilton.",
        budget=400000.00,
        image="https://upload.wikimedia.org/wikipedia/en/thumb/8/83/Hamilton-poster.jpg/220px-Hamilton-poster.jpeg",
        ongoing=False,
    )

    db.session.add(p4)

    db.session.commit()

    c1 = CastMember(name="Example Name", production_id=p1.id)
    c2 = CastMember(name="Example Name 2", production_id=p1.id)
    c3 = CastMember(name="Example Name 3", production_id=p2.id)
    c4 = CastMember(name="Example Name 4", production_id=p2.id)

    db.session.add_all([c1, c2, c3, c4])

    # # 8.✅ Create a query to delete all existing records from Production

    # # 10.✅ Run in terminal:
    # # `python seed.py`
    # # 11.✅ navigate to debug.py
    # # Create doctors
    doctor1 = Doctor(name="Dr. Smith", specialty="Cardiology")
    doctor2 = Doctor(name="Dr. Johnson", specialty="Orthopedics")
    doctor3 = Doctor(name="Dr. Davis", specialty="Dermatology")

    # Create patients
    patient1 = Patient(name="John Doe", email="johndoe@example.com")
    patient2 = Patient(name="Jane Smith", email="janesmith@example.com")
    patient3 = Patient(name="Bob Johnson", email="bobjohnson@example.com")

    date_format = "%Y-%m-%d %H:%M:%S"
    appointment1_date = datetime.strptime("2023-10-10 09:00:00", date_format)
    appointment2_date = datetime.strptime("2023-10-15 14:30:00", date_format)
    appointment3_date = datetime.strptime("2023-10-20 11:15:00", date_format)

    # Create appointments with datetime objects
    appointment1 = Appointment(date=appointment1_date, doctor=doctor1, patient=patient1)
    appointment2 = Appointment(date=appointment2_date, doctor=doctor2, patient=patient2)
    appointment3 = Appointment(date=appointment3_date, doctor=doctor3, patient=patient3)

    # Add the objects to the session and commit to the database
    db.session.add(doctor1)
    db.session.add(doctor2)
    db.session.add(doctor3)
    db.session.add(patient1)
    db.session.add(patient2)
    db.session.add(patient3)
    db.session.add(appointment1)
    db.session.add(appointment2)
    db.session.add(appointment3)
    db.session.commit()
    db.session.commit()
