from datetime import datetime
from flask import abort, make_response

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#print(get_timestamp())

PEOPLE = {
    "Tooth":  {
        "fname": "Tooth",
        "lname": "Fairy",
        "timestamp": get_timestamp(),
    },
    "Santa": {
        "fname": "Santa",
        "lname": "Claus",
        "timestamp": get_timestamp(),
    },
    "Izuku": {
        "fname": "Izuku",
        "lname": "Midoriya",
        "timestamp": get_timestamp(),
    }
}

def read_all_people():
    return list(PEOPLE.values())
#print(read_all_people())

def create_new_person(person):
    lname = person.get("lname")
    fname = person.get("fname",  "")
   #return lname, fname

    if lname and fname not in PEOPLE:
        PEOPLE[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp":  get_timestamp(),
        }
        return PEOPLE[lname], 201
    else:
        abort(
            406,
            f"Person with last name {lname} exists"
        )
# person = {
#     "lname": "human",
#     "fname": "being"
# }
# print(create_new_person(person))

def read_one_person(lname):
    if lname in PEOPLE:
        return PEOPLE[lname]
    else:
        abort(
            404, f"Person with {lname}, does not exist."
        )
    
def update_a_person(lname, person):
    if lname in PEOPLE:
        PEOPLE[lname]["fname"] = person.get("fname", PEOPLE[lname]["fname"])
        PEOPLE[lname]["timestamp"] = get_timestamp()
        return PEOPLE[lname]
    else:
        abort(
            404, f"Person with {lname}, does not exist"
        )

def delete_user_input(lname):
    if lname in PEOPLE:
        del PEOPLE[lname]
        return make_response(
            f"{lname} successfully deleted", 200
        )
    else:
        abort (
            404, f"Person with last name {lname} not found"
        )