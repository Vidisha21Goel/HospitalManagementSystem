# from flask import Flask
# from application.database import db
# app=None
# def create_app():
#     app=Flask(__name__)
#     app.debug=True
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.sqlite3'
#     db.init_app(app)   
#     app.app_context().push()
#     return app
# app=create_app()
# from application.controllers import *
# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#         doctor = User.query.filter_by(username='Doctor1').first()
#         if doctor is None:
#             doctor = User(username='Doctor1', email='doctor1@example.com', password='password', type='doctor')
#             db.session.add(doctor)
#             db.session.commit()
#     app.run(debug=True)

# # from flask import Flask
# # from application.model import db
# # def create_app():
# #     app = Flask(__name__)
# #     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///application/hospital.sqlite3'
# #     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# #     db.init_app(app)
# #     with app.app_context():
# #         db.create_all()
# #         from application.controllers import bp as main_bp
# #         app.register_blueprint(main_bp)
# #     return app

# # if __name__ == '__main__':
# #     app = create_app()
# #     app.run(debug=True)

# # # from application.controllers import app
# # from application.model import db

# # if __name__ == "__main__":
# #     with app.app_context():
# #         db.create_all()
# #     app.run(debug=True)

from flask import Flask
from application.database import db

app = None

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your-secret-key-here'  # Required for sessions
    db.init_app(app)   
    app.app_context().push()
    return app

app = create_app()

# Import models first, then controllers
from application.models import User
from application.controllers import *

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        doctor = User.query.filter_by(username='Doctor1').first()
        if doctor is None:
            doctor = User(username='Doctor1', email='doctor1@example.com', password='password', type='doctor')
            db.session.add(doctor)
            db.session.commit()
            print("Doctor1 user created successfully!")
    app.run(debug=True)