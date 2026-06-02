from core import *

def activities_user(data, user):
    exist_user_activities =  activities_exist(data, user)

    if exist_user_activities == False:
       return {"status":"error", "message": "no activities of user"}
        
        
    user_activities = get_activities(data, user)
    
    return {"status": "ok", "activities": user_activities}