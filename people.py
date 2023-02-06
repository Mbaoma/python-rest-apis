from flask import abort, make_response
from config import db
from models import Person, people_schema, person_schema

def read_all_people():
    people = Person.query.all()
    return people_schema.dump(people)

def read_one_person(lname):
    person = Person.query.filter(Person.lname == lname).one_or_none()

    if person is not None:
        return person_schema.dump(person)
    else:
        abort(
            404, f"Person with last name {lname}, does not exist."
        )

def create_new_person(person):
    lname = person.get("lname")
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()

    if existing_person is None:
        new_person = person_schema.load(person, session=db.session)
        db.session.add(new_person)
        db.session.commit()
        return person_schema.dump(new_person), 201
    else:
        abort(
            406,
            f"Person with last name {lname} exists"
        )
    
def update_a_person(lname, person):
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()

    if  existing_person:
        update_person = person_schema.load(person, session=db.session)
        existing_person.fname = update_person.fname
        db.session.merge(existing_person)
        db.session.commit()
        return person_schema.dump(existing_person),201
    else:
        abort(
            404, f"Person with last name {lname}, does not exist"
        )

def delete_user_input(lname):
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()
    
    if existing_person:
        db.session.delete(existing_person)
        db.session.commit()
        return make_response(
            f"{lname} successfully deleted", 200
        )
    else:
        abort (
            404, f"Person with last name {lname} not found"
        )