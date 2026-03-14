# # from flask import Flask
# # from app.services.db import mysql
 


# # def create_app():

# #     app = Flask(__name__)

# #     app.config["MYSQL_HOST"] = "localhost"
# #     app.config["MYSQL_USER"] = "root"
# #     app.config["MYSQL_PASSWORD"] = "root123"
# #     app.config["MYSQL_DB"] = "hospital_db"

# #     mysql.init_app(app)

# #     # IMPORT ROUTES
# #     from app.routes.doctor_routes import doctor_bp
# #     from app.routes.auth_routes import auth_bp

# #     # REGISTER BLUEPRINTS
# #     app.register_blueprint(doctor_bp)
# #     app.register_blueprint(auth_bp)

# #     return app


   

# from flask import Flask
# from app.services.db import mysql
# import os

# def create_app():
#     app = Flask(__name__)

#     # ✅ Set a secret key for session and flash
#     # You can use os.urandom(24) for randomness
#     app.secret_key = os.urandom(24)

#     # MySQL config
#     app.config["MYSQL_HOST"] = "localhost"
#     app.config["MYSQL_USER"] = "root"
#     app.config["MYSQL_PASSWORD"] = "root123"
#     app.config["MYSQL_DB"] = "hospital_db"

#     # Initialize MySQL
#     mysql.init_app(app)

#     # Import routes
#     from app.routes.doctor_routes import doctor_bp
#     from app.routes.auth_routes import auth_bp

#     # Register blueprints
#     app.register_blueprint(doctor_bp)
#     app.register_blueprint(auth_bp)

#     return app


from flask import Flask
from app.services.db import mysql

def create_app():

    app = Flask(__name__)

    app.secret_key = "hospital_secret_key"

    app.config["MYSQL_HOST"] = "localhost"
    app.config["MYSQL_USER"] = "root"
    app.config["MYSQL_PASSWORD"] = "root123"
    app.config["MYSQL_DB"] = "hospital_db"

    mysql.init_app(app)

    from app.routes.doctor_routes import doctor_bp
    from app.routes.auth_routes import auth_bp
    from app.routes.appointment_routes import appointment_bp

    app.register_blueprint(doctor_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(appointment_bp)

    return app