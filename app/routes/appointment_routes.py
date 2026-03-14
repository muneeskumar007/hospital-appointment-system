


from flask import Blueprint, session, redirect, render_template
from app.services.db import mysql

appointment_bp = Blueprint("appointment", __name__)


@appointment_bp.route("/book/<int:doctor_id>")
def book_appointment(doctor_id):

    if "user" not in session:
        return redirect(url_for("auth.login"))

    return f"Appointment confirmed with doctor ID {doctor_id}"