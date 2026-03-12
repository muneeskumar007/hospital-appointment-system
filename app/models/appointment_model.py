class Appointment:
    def __init__(self, id, patient_id, doctor_id, date, time, status):
        self.id = id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.time = time
        self.status = status