from .database import db, migrate
from .registration import register

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)
    return app

# Create Flask application
app = create_app()

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/patients'

# Initialize SQLAlchemy with the Flask application
db.init_app(app)

# Initialize Flask-Migrate with the Flask application and SQLAlchemy
migrate.init_app(app, db)

# Register the blueprint with the Flask application
register(app)

@app.route('/heartbeat')
def heartbeat():
    return "Service is Up and Running"
