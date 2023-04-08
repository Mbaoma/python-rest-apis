from datetime import datetime
from config import app, db
from models import Person, Note

PEOPLE_NOTES = [
    {
        "lname":"John",
        "fname": "W",
        "notes": [
            ("John is an avid reader and enjoys spending his weekends curled up with a good book and a cup of tea", "2023-02-04 14:15"),
            ("He particularly enjoys science fiction and fantasy novels that transport him to other worlds and immerse him in exciting adventures.", "2023-02-04 14:15" ),
        ],
    },
    {
        "lname": "Sarah",
        "fname": "T",
        "notes": [
            ("Sarah is a talented musician and spends most of her free time writing and performing her own songs", "2023-02-04 14:15"),
            ("She is an avid traveler and has visited over 20 countries in the past five years.", "2023-02-04 14:15"),
        ],
    },
    {
        "lname": "Mark",
        "fname": "B",
        "notes": [
            ("Mark is a computer programmer who enjoys learning new coding languages and building websites in his spare time.", "2023-02-04 14:15"),
            ("Mark has recently started working on a new web application that he hopes to launch in the near future, and he spends most of his evenings and weekends working on it.", "2023-02-04 14:15"),
        ],
    },
    {
        "lname": "Emily",
        "fname": "E",
        "notes": [
            ("Emily is a fitness enthusiast and enjoys trying out new workout classes and exploring different hiking trails in her area.", "2023-02-04 14:15"),
            ("Her favorite hobby is woodworking, and she has built several pieces of furniture for her home", "2023-02-04 14:15"),
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
