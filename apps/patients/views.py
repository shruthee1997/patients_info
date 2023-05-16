from flask import jsonify, make_response, request
from flask.views import MethodView

from .service import get_patient, insert_patient, update_patient, delete_patient

class PatientsAPI(MethodView):
    def get(self, patientId= None):
        patients = get_patient(patientId)
        if isinstance(patients, list):
            return make_response(jsonify([patient.serialize() for patient in patients]))
        else:
            return make_response(jsonify(patients.serialize()))

    def post(self):
        data = request.get_json()
        patient = insert_patient(data)
        return make_response(jsonify(patient.serialize()), 201)

    def put(self, patientId):
        data = request.get_json()
        patient = update_patient(patientId, data)
        return make_response(patient.serialize(), 200)

    def delete(self, patientId):
        delete_patient(patientId)
        return make_response('', 204)
