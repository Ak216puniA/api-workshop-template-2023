from db import last_id_assigned

def increment_id():
    global last_id_assigned
    last_id_assigned += 1

    return last_id_assigned