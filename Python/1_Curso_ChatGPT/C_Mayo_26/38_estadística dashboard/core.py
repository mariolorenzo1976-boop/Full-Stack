def clean_data(data):

    clean_data_list = []
    
    if not data:
        return []
    
    for n in data:
        if "user" in n and "sport" in n and "km" in n and isinstance(n, dict) and \
           isinstance(n["user"], str)  and isinstance(n["sport"], str) and \
           isinstance(n["km"], (int,float)):
            
           clean_data_list.append(n) 

            
    return clean_data_list

def acumulator_for_km(acumulator,data):

    var_acumulator = {}
    apy_acumulator = []

    for n in data:
        if n[acumulator] not in var_acumulator:
           var_acumulator[n[acumulator]] = 0
        var_acumulator[n[acumulator]] += n["km"]

    for name, km in var_acumulator.items():
        apy_acumulator.append({acumulator: name, "km": km})

    return apy_acumulator

           
        
def top_for_km(filter,data):

    top_km = 0
    var_filter = None

    for n in data:
        if n["km"] > top_km:
            top_km = n["km"]
            var_filter = {filter: n[filter], "km": top_km}
            

    return var_filter