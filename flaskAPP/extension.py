def send_response(message=None, status_code=200, data={}):
    return {"message": message,
            "status_code": status_code,
            "data": data}