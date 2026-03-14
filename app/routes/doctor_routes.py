from flask import Blueprint, render_template
from app.config import get_db_connection

doctor_bp = Blueprint('doctor', __name__)

# Doctor List Page
@doctor_bp.route('/doctors')
def doctors():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM doctors")
    doctors = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("doctors.html", doctors=doctors)


# Doctor Profile Page
@doctor_bp.route('/doctor/<int:id>')
def doctor_profile(id):

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM doctors WHERE id = %s", (id,))
    doctor = cursor.fetchone()

    cursor.close()
    conn.close()

    return render_template("doctor_profile.html", doctor=doctor)