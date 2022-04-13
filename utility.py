import os
import json

def get_location():
    location = os.path.dirname(os.path.realpath(__file__)
    return location

def get_data(str_txt):
    data = json.load(str_txt)
    return data
