
def valid_data_schema(data):

    if not data:
        return {"status" :"error",
                "message": "no data: empty"
                }
    
    if "user" not in data:
        return {"status" :"error",
                "message": "missing field user"
                }

    if "sport" not in data: 
        return {"status" :"error",
                "message": "missing field sport"
                }
    
    
    if "km" not in data:
        return {"status" :"error",
                "message": "missing field km"
                }
        
        
    if isinstance(data, dict) and isinstance(data["user"], str) and isinstance(data["sport"], str) and \
       isinstance(data["km"], (int,float)):

       return {"status" :"ok"}
    else:
       return {"status" :"error"}
    

def valid_data_bussines(data, data_sport):

    if data["sport"] not in data_sport:
        return {"status" :"error",
                "message": "incorrect sport"
                }

    if data["km"] < 0:
        return {"status" :"error",
                "message": "incorrect km"
                }
    
    return {"status": "ok"}


def add_data(data,new_activitie):

      
        
    data["activities"].append(new_activitie)
  
    return {"status" :"ok", "database" :data}

        