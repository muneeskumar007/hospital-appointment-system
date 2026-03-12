from app.routes.patient_routes import patient_bp
from app.routes.doctor_routes import doctor_bp

app.register_blueprint(patient_bp)
app.register_blueprint(doctor_bp)

from flask import Flask
from app.config import get_db_connection

from app.routes.auth_routes import auth_bp

app = Flask(__name__)
app.secret_key = "hospital_secret_key"


app.register_blueprint(auth_bp)

@app.route("/")
def home():
    return "Hospital Appointment System Home Page"


conn = get_db_connection()
print("Database connected successfully")
conn.close()







if __name__ == "__main__":
    app.run(debug=True)
