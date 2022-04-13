import os
import json

def get_location():
    location = os.path.dirname(os.path.realpath(__file__)
    return location

def get_data(txt):
    data = json.load(txt)
    return data

def get_user_in_lower(name):
    name=name.lower()
    return name
