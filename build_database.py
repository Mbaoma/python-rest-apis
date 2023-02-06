from datetime import datetime
from config import app, db
from models import Person, Note

PEOPLE_NOTES = [
    {
        "lname":"Lu",
        "fname": "Bu",
        "notes": [
            ("Ga kou", "2023-02-04 14:15"),
            ("You are so cool", "2023-02-04 14:15"),
        ],
    },
    {
        "lname": "Beifong",
        "fname": "Toph",
        "notes": [
            ("The GOAT", "2023-02-04 14:15"),
            ("Greatest bender", "2023-02-04 14:15"),
        ],
    },
    {
        "lname": "Hanma",
        "fname": "Baki",
        "notes": [
            ("My hero", "2023-02-04 14:15"),
            ("I hope you win", "2023-02-04 14:15"),
        ],
    },
    {
        "lname": "Uzumaki",
        "fname": "Naruto",
        "notes": [
            ("My Hokage", "2023-02-04 14:15"),
            ("Nandebayor", "2023-02-04 14:15"),
        ],
    },
]

with app.app_context():
    db.drop_all()
    db.create_all()
    for data in PEOPLE_NOTES:
        new_person = Person(lname=data.get("lname"), fname=data.get("fname"))
        for content, timestamp in data.get("notes", []):
            new_person.notes.append(
                Note(
                    content=content,
                    timestamp=datetime.strptime(timestamp, "%Y-%m-%d %H:%M")
                )
            )
        db.session.add(new_person)
    db.session.commit()
