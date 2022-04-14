import os
import json
import subprocess
import multithreading

class Utility(object):
    def __init__(self,func):
        self.func = func

    def get_location(self):
       location = os.path.dirname(os.path.realpath(__file__)
       return location

    def get_data(self,txt):
       data = json.load(txt)
       return data

    def get_user_in_lower(self,name):
       name=name.lower()
       return name

    def get_user_in_capital(self,name):
       name=name.upper()
       return name
    
