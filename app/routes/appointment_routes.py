from flask import Blueprint,render_template,request,redirect,url_for
from app.services.appointment_service import *

appointment_bp = Blueprint('appointment',__name__)

@appointment_bp.route("/appointment")

def appointment_page():
    return render_template("appointment.html")


@appointment_bp.route("/book",methods=["POST"])
def book():

    patient_id = request.form["patient_id"]
    doctor_id = request.form["doctor_id"]
    date = request.form["date"]
    time = request.form["time"]

    book_appointment(patient_id,doctor_id,date,time)

    return redirect("/appointment")


@appointment_bp.route("/myappointments/<int:patient_id>")

def myappointments(patient_id):

    data = get_patient_appointments(patient_id)

    return render_template("appointment.html",appointments=data)


@appointment_bp.route("/cancel/<int:id>")

def cancel(id):

    cancel_appointment(id)

    return redirect("/appointment")