import json
from random import randint, random
from itertools import groupby


class Game:
    def __init__(self, name, skill=50):
        self.name = name
        self.skill = skill
        self.luck = 100 - skill
    
    def set_property(self, property_name, value):
        setattr(self, property_name, value)
        
    def __str__(self):
        return self.__class__.__name__ + ': ' + json.dumps(self.__dict__)
    
    def compete(self, player_list):
        for player in player_list:
            player.score = self.score(player)
        sorted_list = sorted(player_list, key=lambda x: x.score, reverse=True)
        grouped = groupby(sorted_list, key=lambda x: x.score)
        results = []
        for key, group in grouped:
            tied = list(group)
            if len(tied) > 1:
                results.extend(self.compete(tied)) # tiebreaker!
            else:
                results.extend(tied)
        return results

    def score(self, player):
        return 0.005 * (self.skill * randint(1,player.rating) + self.luck * randint(1,player.luckiness))
            