
from flask import Blueprint, render_template, session
from app.services.db import mysql

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/dashboard")
def dashboard():

    cur = mysql.connection.cursor()

    cur.execute(
    """SELECT doctors.name, appointments.token
    FROM appointments
    JOIN doctors ON doctors.id=appointments.doctor_id
    WHERE patient_id=%s""",
    (session["user_id"],)
    )

    appointments = cur.fetchall()

    return render_template("dashboard.html",appointments=appointments)