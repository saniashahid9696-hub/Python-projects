class Patient:
    def __init__(self, name, patient_id, age, disease):
        self.name = name
        self.patient_id = patient_id
        self.age = age
        self.disease = disease

    def view_details(self):
        print("\nPatient Details:")
        print(f"Name: {self.name}")
        print(f"Patient ID: {self.patient_id}")
        print(f"Age: {self.age}")
        print(f"Disease: {self.disease}")


class Doctor:
    def __init__(self, name, doctor_id, specialization):
        self.name = name
        self.doctor_id = doctor_id
        self.specialization = specialization


class Appointment:
    def __init__(self, patient, doctor, appointment_date):
        self.patient = patient
        self.doctor = doctor
        self.appointment_date = appointment_date

    def book_appointment(self):
        print("\nAppointment Booked Successfully!")
        print(f"Patient: {self.patient.name}")
        print(f"Doctor: {self.doctor.name} ({self.doctor.specialization})")
        print(f"Date: {self.appointment_date}")


# Example usage
patient1 = Patient("Ali", 1, 30, "Fever")
doctor1 = Doctor("Dr. Sara", 101, "General Physician")

appointment1 = Appointment(patient1, doctor1, "2026-03-05")

# Assign doctor & book appointment
appointment1.book_appointment()

# View patient details
patient1.view_details()