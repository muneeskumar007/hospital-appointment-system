


from flask import Blueprint, session, redirect, render_template
from app.services.db import mysql

appointment_bp = Blueprint("appointment", __name__)

@appointment_bp.route("/book/<int:doctor_id>/<int:slot_id>")
def book(doctor_id,slot_id):

    if "user_id" not in session:
        return redirect("/login")

    cur = mysql.connection.cursor()

    cur.execute(
    "SELECT COUNT(*) FROM appointments WHERE doctor_id=%s",
    (doctor_id,)
    )

    token = cur.fetchone()[0] + 1

    cur.execute(
    """INSERT INTO appointments
    (patient_id,doctor_id,slot_id,token,status)
    VALUES(%s,%s,%s,%s,'Booked')""",
    (session["user_id"],doctor_id,slot_id,token)
    )

    mysql.connection.commit()

    return render_template("token.html",token=token)