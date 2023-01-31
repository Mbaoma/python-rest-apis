from datetime import datetime
from config import db, marshmallow_app

class Person(db.Model):
    __tablename__ = "person"
    id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32), unique=True)
    fname = db.Column(db.String(32))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class PersonSchema(marshmallow_app.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        load_instance = True
        sql_session = db.session

person_schema = PersonSchema()
people_schema = PersonSchema(many=True)

