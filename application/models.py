# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(150), unique=True, nullable=False)
#     email = db.Column(db.String(150), unique=True, nullable=False)
#     password = db.Column(db.String(150), nullable=False)
#     type = db.Column(db.String(20), nullable=False)  # admin, doctor, patient
#     patient = db.relationship('Patient', backref='user', uselist=False)
#     doctor = db.relationship('Doctor', backref='user', uselist=False)

# class Patient(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     # add contact or other patient specific fields if needed

# class Doctor(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     specialization = db.Column(db.String(150))
#     department = db.Column(db.String(150))
#     experience = db.Column(db.Integer)
#     # You may add availability fields too

# class Appointment(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
#     doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=False)
#     date = db.Column(db.String(50))
#     time = db.Column(db.String(50))
#     status = db.Column(db.String(20))  # Booked/Completed/Cancelled
#     treatment_id = db.Column(db.Integer, db.ForeignKey('treatment.id'))

# class Treatment(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     diagnosis = db.Column(db.String(500))
#     prescription = db.Column(db.String(500))
#     notes = db.Column(db.String(500))
#     appointment = db.relationship('Appointment', backref='treatment', uselist=False)

from application.database import db

class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)  # In production, use hashed passwords!
    type = db.Column(db.String(20), nullable=False)  # 'doctor', 'patient', 'admin', etc.
    
    def __repr__(self):
        return f'<User {self.username}>'