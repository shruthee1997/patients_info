from apps.patients.urls import patients_bp

# Register the blueprint with the Flask application
def register(app):
    app.register_blueprint(patients_bp)