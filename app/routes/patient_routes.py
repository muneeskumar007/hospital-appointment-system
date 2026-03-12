from flask import Blueprint, render_template
from app.models.doctor_model import DoctorModel
from flask import current_app

patient_bp = Blueprint("patient", __name__)

@patient_bp.route("/patient/dashboard")
def patient_dashboard():
    mysql = current_app.mysql
    doctors = DoctorModel.get_all_doctors(mysql)

    return render_template("patient_dashboard.html", doctors=doctors)