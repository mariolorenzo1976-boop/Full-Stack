from core import *

def add_valid_data(data, data_sport):

    validation_shema = (valid_data_schema(data))
    
    if validation_shema["status"] == "error":
       return validation_shema 

    validation_bussines = (valid_data_bussines(data, data_sport))
    
    if validation_bussines["status"] == "error":
        return validation_bussines
    
    # if validation_bussines["status"] =="error":
    #     return validation_bussines
    
    add_register = (add_data(data))

    return add_register