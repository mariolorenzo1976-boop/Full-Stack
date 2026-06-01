from core import *

# a litlel stadistic: "total of total activities kms" , "count of activities", "favourite sport"
def stadistic(user, data):

    clean_data_user = clean_data(user, data)
    total_km_user = total_km(clean_data_user)
    amount_activities_user = amount_activities(clean_data_user)
    favorite_sport_user = favorite_sport(clean_data_user)

    out_data_user = {"user":user, "total km": total_km_user, "activities": amount_activities_user, "favorite_sport": favorite_sport_user}
    
    return  out_data_user

# my valid activities
def my_activities(user,data):
   
    clean_data_user = clean_data(user, data)
    my_activities_user = valid_sport(clean_data_user)

    return my_activities_user

# my filters for activities
def my_activities_filter(user,data,sport):

     clean_data_user = clean_data(user, data)
     my_activities_filter_sport = filter_sport(clean_data_user, sport)

     return my_activities_filter_sport

