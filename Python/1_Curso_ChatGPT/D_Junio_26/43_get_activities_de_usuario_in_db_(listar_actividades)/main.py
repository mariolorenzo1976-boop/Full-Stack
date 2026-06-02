import json
from apy import *
from data import *

print(json.dumps(activities_user(database, "mario"), indent=4))