def send_response(message=None, status_code=200, data={}):
    return {"message": message,
            "status_code": status_code,
            "data": data}


### Dummy Database

user_database = [
    {"id":1,
    "username":"admin",
    "password":"admin123"},
    {"id":2,
    "username":"joy",
    "password":"joy123"},
    {"id":3,
    "username":"dip",
    "password":"dip123"}
]