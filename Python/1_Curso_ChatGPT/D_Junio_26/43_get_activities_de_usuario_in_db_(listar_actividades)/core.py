
def activities_exist(data, user):

    if not data:
        return False
    
    for n in data["activities"]:
        if n["user"] == user:
            return True
    return False


def get_activities(data, user):

    activities = []

    for n in data["activities"]:
        if n["user"] == user:
            activities.append(n)

    return activities