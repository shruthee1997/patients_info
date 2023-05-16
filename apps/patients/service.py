from .models import get_all, insert, update, delete

def get_patient(patient_id):
    patient = get_all(patient_id)
    return patient

def insert_patient(data):
    patient = insert(data)
    return patient

def update_patient(patient_id, data):
    patient = update(patient_id, data)
    return patient

def delete_patient(patient_id):
    patient = delete(patient_id)
