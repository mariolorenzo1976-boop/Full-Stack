import json
import os

BASE_DIR = os.path.dirname(__file__)
FILE_PATH = os.path.join(BASE_DIR, "data.json")

with open(FILE_PATH, "r") as file:
    data = json.load(file)