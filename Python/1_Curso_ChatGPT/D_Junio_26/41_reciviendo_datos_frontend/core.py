
def valid_data(data):

    if not data:
        return {}
    
    if "user" in data and "sport" in data and "km" in data and isinstance(data, dict) and \
       isinstance(data["user"], str) and isinstance(data["sport"], str) and \
       isinstance(data["km"], (int,float)):

       return {"status" :"ok"}
    else:
       return {"status" :"error"}


def add_data(data, validation):

    validation_data = validation["status"]
    add_data_register = {}
    
    if validation_data == "ok":
        add_data_register = data
        return add_data_register, validation
    else:
        return validation

        