from app.routes.patient_routes import patient_bp
from app.routes.doctor_routes import doctor_bp

app.register_blueprint(patient_bp)
app.register_blueprint(doctor_bp)