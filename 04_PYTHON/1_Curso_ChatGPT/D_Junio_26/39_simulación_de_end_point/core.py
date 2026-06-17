

def clean_data(user, data):

    clean_data_user = []

    if not data:
        return []
    
    for n in data:
        if isinstance(n, dict)and "user" in n and "sport" in n and "km" in n and n["user"] == user and \
           isinstance(n["user"], str) and isinstance(n["sport"], str) and isinstance(n["km"], (int,float)):
            
            clean_data_user.append(n)

    return clean_data_user


def total_km(data):

    total_counter_km = 0
    
    for n in data:
       total_counter_km += n["km"] 
    

    return total_counter_km


def amount_activities(data):

    amount_activities_user = len(data)
    return(amount_activities_user)


def favorite_sport(data):

    sport_acumulator = {}
    counter = 0

    if not data:
        return None
    
    for n in data:
        if not n["sport"] in sport_acumulator:
            sport_acumulator[n["sport"]] = 0
        sport_acumulator[n["sport"]] += 1

    for key, value in sport_acumulator.items():
        if value > counter:
            counter = value
            favorite_sport = key

    return favorite_sport

