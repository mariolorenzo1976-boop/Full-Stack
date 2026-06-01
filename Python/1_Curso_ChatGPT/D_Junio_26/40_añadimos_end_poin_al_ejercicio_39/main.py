from data import *
from apy import *
import json

# call litlel stadistic for user
print(json.dumps(stadistic("mario", data), indent = 4))

# call all valid activities for user
print(json.dumps(my_activities("mario", data), indent = 4))

# call all valid activities for user and sport filter
print(json.dumps(my_activities_filter("mario", data, "bike"), indent = 4))
