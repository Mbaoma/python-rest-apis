import pathlib
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 

base_directory = pathlib.Path(__file__).parent.resolve()
connexion_app = connexion.App(__name__, specification_dir=base_directory)

app = connexion_app.app
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{base_directory / 'people.db'}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
marshmallow_app = Marshmallow(app)

