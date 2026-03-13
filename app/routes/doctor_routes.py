from flask import Blueprint, render_template
from app.services.db import mysql

doctor_bp = Blueprint("doctor", __name__)

@doctor_bp.route("/doctor/<int:id>")
def doctor_profile(id):

    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM doctors WHERE id=%s",(id,))
    d = cur.fetchone()

    doctor = {
        "id": d[0],
        "name": d[1],
        "specialty": d[2],
        "experience": d[3],
        "fee": d[4]
    }

    cur.execute("SELECT * FROM slots WHERE doctor_id=%s",(id,))
    slots = cur.fetchall()

    slot_list = []

    for s in slots:
        slot_list.append({
            "id": s[0],
            "time": s[2]
        })

    return render_template("doctor_profile.html",doctor=doctor,slots=slot_list)