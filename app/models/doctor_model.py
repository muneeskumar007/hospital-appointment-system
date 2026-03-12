from flask_mysqldb import MySQL

class DoctorModel:

    @staticmethod
    def get_all_doctors(mysql):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM doctors")
        doctors = cursor.fetchall()
        cursor.close()
        return doctors