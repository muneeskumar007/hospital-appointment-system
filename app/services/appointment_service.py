import mysqldb
from flask import current_app

def get_db():
    return mysqldb.connect(
        host="localhost",
        user="root",
        passwd="",
        db="hospital_db"
    )


def book_appointment(patient_id, doctor_id, date, time):
    db = get_db()
    cursor = db.cursor()

    query = """
    INSERT INTO appointments (patient_id, doctor_id, appointment_date, appointment_time)
    VALUES (%s,%s,%s,%s)
    """

    cursor.execute(query,(patient_id,doctor_id,date,time))
    db.commit()
    db.close()


def get_patient_appointments(patient_id):

    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM appointments WHERE patient_id=%s",
        (patient_id,)
    )

    data = cursor.fetchall()
    db.close()

    return data


def cancel_appointment(id):

    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "DELETE FROM appointments WHERE id=%s",
        (id,)
    )

    db.commit()
    db.close()