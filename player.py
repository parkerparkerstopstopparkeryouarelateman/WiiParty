import json

class Player:
    def __init__(self, name, rating=50, luckiness=0):
        self.name = name
        self.rating = rating
        self.luckiness = luckiness
    
    def set_property(self, property_name, value):
        setattr(self, property_name, value)
        
    def __str__(self):
        return self.__class__.__name__ + ': ' + json.dumps(self.__dict__)
    