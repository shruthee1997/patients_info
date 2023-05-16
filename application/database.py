from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Create an instance of SQLAlchemy
db = SQLAlchemy()


migrate = Migrate()