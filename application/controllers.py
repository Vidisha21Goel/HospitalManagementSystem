# from flask import Flask, render_template, request, redirect, url_for, session
# from .model import db, User, Patient, Doctor, Appointment, Treatment
# import os

# app = Flask(__name__)

# app.config['SECRET_KEY'] = 'Vidisha@21'  # Change in production
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.getcwd(), 'instance', 'hospital.sqlite3')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db.init_app(app)

# @app.route('/')
# def home():
#     return redirect(url_for('login'))

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == "POST":
#         username = request.form.get('username')
#         password = request.form.get('pwd')
#         user = User.query.filter_by(username=username).first()
#         if user and user.password == password:
#             session['user_id'] = user.id
#             session['user_type'] = user.type
#             if user.type == 'admin':
#                 return redirect(url_for('admin_dash'))
#             elif user.type == 'doctor':
#                 return redirect(url_for('doctor_dash'))
#             elif user.type == 'patient':
#                 return redirect(url_for('patient_dash'))
#         elif user:
#             return render_template('incorrect_p.html')
#         else:
#             return render_template('incorrect_user.html')
#     return render_template('login.html')

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == "POST":
#         username = request.form.get('username')
#         email = request.form.get('email')
#         password = request.form.get('pwd')
#         if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
#             return render_template('already.html')
#         new_user = User(username=username, email=email, password=password, type='patient')
#         db.session.add(new_user)
#         db.session.commit()
#         patient = Patient(user_id=new_user.id)
#         db.session.add(patient)
#         db.session.commit()
#         return redirect(url_for('login'))
#     return render_template('register.html')

# @app.route('/admin')
# def admin_dash():
#     doctors = Doctor.query.all()
#     patients = Patient.query.all()
#     appointments = Appointment.query.all()
#     return render_template('admin_dash.html', doctors=doctors, patients=patients, appointments=appointments)

# @app.route('/doctor')
# def doctor_dash():
#     user_id = session.get('user_id')
#     if not user_id:
#         return redirect(url_for('login'))
#     user = User.query.get(user_id)
#     doctor = user.doctor if user and user.type == 'doctor' else None
#     if not doctor:
#         return redirect(url_for('login'))
#     appointments = Appointment.query.filter_by(doctor_id=doctor.id).all()
#     return render_template('doctor_dash.html', doctor=doctor, appointments=appointments)

# @app.route('/patient')
# def patient_dash():
#     user_id = session.get('user_id')
#     if not user_id:
#         return redirect(url_for('login'))
#     user = User.query.get(user_id)
#     patient = user.patient if user and user.type == 'patient' else None
#     if not patient:
#         return redirect(url_for('login'))
#     appointments = Appointment.query.filter_by(patient_id=patient.id).all()
#     return render_template('patient_dash.html', patient=patient, appointments=appointments)

# @app.route('/logout')
# def logout():
#     session.clear()
#     return redirect(url_for('login'))


from flask import render_template, request, redirect, url_for, session, flash
from application.database import db
from application.models import User
from app import app

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('pwd')
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.password == password:
            session['user_id'] = user.id
            session['username'] = user.username
            session['user_type'] = user.type
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'error')
            return render_template('login.html', error='Invalid credentials')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        user_type = request.form.get('type', 'patient')
        
        # Check if user already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists', 'error')
            return render_template('register.html', error='Username already exists')
        
        # Create new user
        new_user = User(username=username, email=email, password=password, type=user_type)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session.get('username'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))