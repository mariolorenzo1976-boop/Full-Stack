from core import *


def stadistic(user, data):

    clean_data_user = clean_data(user, data)
    total_km_user = total_km(clean_data_user)
    amount_activities_user = amount_activities(clean_data_user)
    favorite_sport_user = favorite_sport(clean_data_user)

    out_data_user = {"user":user, "total km": total_km_user, "activities": amount_activities_user, "favorite_sport": favorite_sport_user}
    
    return  out_data_user