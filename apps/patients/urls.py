from .views import PatientsAPI

from flask import Blueprint

# Define a blueprint
patients_bp = Blueprint('patients_bp', __name__,)

# Register routes, views, etc. with the blueprint
patients_bp.add_url_rule("/patients", view_func=PatientsAPI.as_view("patients"))
patients_bp.add_url_rule("/patients/<string:patientId>", view_func=PatientsAPI.as_view("patients_id"))