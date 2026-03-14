


# from flask import Blueprint, render_template, session, redirect, url_for, request
# from app.services.db import mysql

# doctor_bp = Blueprint("doctor", __name__)


# # HOME PAGE
# @doctor_bp.route("/")
# def home():

#     cur = mysql.connection.cursor()
#     cur.execute("SELECT id,name,specialty,experience,fee FROM doctors")
#     rows = cur.fetchall()

#     doctors = []

#     for r in rows:
#         doctors.append({
#             "id": r[0],
#             "name": r[1],
#             "specialty": r[2],
#             "experience": r[3],
#             "fee": r[4]
#         })

#     return render_template("index.html", doctors=doctors)


# # DOCTORS LIST PAGE
# @doctor_bp.route("/doctors")
# def doctors():

#     cur = mysql.connection.cursor()
#     cur.execute("SELECT id,name,specialty,experience,fee FROM doctors")
#     rows = cur.fetchall()

#     doctors = []

#     for r in rows:
#         doctors.append({
#             "id": r[0],
#             "name": r[1],
#             "specialty": r[2],
#             "experience": r[3],
#             "fee": r[4]
#         })

#     return render_template("doctors.html", doctors=doctors)


# # SINGLE DOCTOR PROFILE
# @doctor_bp.route("/doctor/<int:id>")
# def doctor_profile(id):

#     # check login
#     if "user_id" not in session:
#         return redirect(url_for("auth.login", next=request.url))

#     cur = mysql.connection.cursor()

#     cur.execute(
#         "SELECT id,name,specialty,experience,fee FROM doctors WHERE id=%s",
#         (id,)
#     )

#     r = cur.fetchone()

#     if not r:
#         return "Doctor not found"

#     doctor = {
#         "id": r[0],
#         "name": r[1],
#         "specialty": r[2],
#         "experience": r[3],
#         "fee": r[4]
#     }

#     return render_template("doctor.html", doctor=doctor)



from flask import Blueprint, render_template, session, redirect, url_for, request
from app.services.db import mysql

doctor_bp = Blueprint("doctor", __name__)


# HOME PAGE
@doctor_bp.route("/")
def home():

    cur = mysql.connection.cursor()
    cur.execute("SELECT id,name,specialty,experience,fee FROM doctors")
    rows = cur.fetchall()

    doctors = []

    for r in rows:
        doctors.append({
            "id": r[0],
            "name": r[1],
            "specialty": r[2],
            "experience": r[3],
            "fee": r[4]
        })

    return render_template("index.html", doctors=doctors)


# DOCTORS LIST PAGE
@doctor_bp.route("/doctors")
def doctors():

    cur = mysql.connection.cursor()
    cur.execute("SELECT id,name,specialty,experience,fee FROM doctors")
    rows = cur.fetchall()

    doctors = []

    for r in rows:
        doctors.append({
            "id": r[0],
            "name": r[1],
            "specialty": r[2],
            "experience": r[3],
            "fee": r[4]
        })

    return render_template("doctors.html", doctors=doctors)


# SINGLE DOCTOR PROFILE
@doctor_bp.route("/doctor/<int:id>")
def doctor_profile(id):

    if "user_id" not in session:
        return redirect(url_for("auth.login", next=request.url))

    cur = mysql.connection.cursor()

    cur.execute(
        "SELECT id,name,specialty,experience,fee FROM doctors WHERE id=%s",
        (id,)
    )

    r = cur.fetchone()

    if not r:
        return "Doctor not found"

    doctor = {
        "id": r[0],
        "name": r[1],
        "specialty": r[2],
        "experience": r[3],
        "fee": r[4]
    }

    return render_template("doctor.html", doctor=doctor)