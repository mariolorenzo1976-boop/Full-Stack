from core import *

def new_activity(database, new_activitie, data_sport):

    validation_shema = (valid_data_schema(new_activitie))
    
    if validation_shema["status"] == "error":
       return validation_shema 

    validation_bussines = (valid_data_bussines(new_activitie, data_sport))
    
    if validation_bussines["status"] == "error":
        return validation_bussines
    
    # if validation_bussines["status"] =="error":
    #     return validation_bussines
    
    add_register = (add_data(database,new_activitie))

    return add_register