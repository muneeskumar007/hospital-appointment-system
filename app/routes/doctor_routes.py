from flask import Blueprint, render_template

doctor_bp = Blueprint("doctor", __name__)

@doctor_bp.route("/doctor/dashboard")
def doctor_dashboard():
    return render_template("doctor_dashboard.html")