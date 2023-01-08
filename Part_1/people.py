from datetime import datetime

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#print(get_timestamp())

PEOPLE = {
    "Fairy":  {
        "fname": "Tooth",
        "lname": "Fairy",
        "timestamp": get_timestamp(),
    },
    "Santa": {
        "fname": "Santa",
        "lname": "Claus",
        "timestamp": get_timestamp(),
    },
    "Deku": {
        "fname": "Izuku",
        "lname": "Midoriya",
        "timestamp": get_timestamp(),
    }
}

def read_all_people():
    return list(PEOPLE.values())
#print(read_all_people())