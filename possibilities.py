#!/usr/bin/python3
import random
import game_config
"""
This file is like "dice roll" for some events in "life".
"""


class Events(object):
    """Allways return True or False based on chance
    :param age: <int> age of human object
    :param args: <int> positive or negative influence to chance
    """
    def __init__(self):
        self.chance = 0

    def make_decision(self, chance):
        """Roll the dice
        
        :param chance: <int> 
        :return: True/False
        """
        return random.randrange(1000) <= chance

    def death(self, age):
        i = int(age / game_config.LIFE_PART) - 1  # -- i is just a support variable
        chance = self.chance + game_config.NATURAL_DEATH_CHANCES[i]
        return self.make_decision(chance)

    def have_offspring(self, age):
        fertility_life_period = (game_config.MAX_HUMAN_AGE - game_config.FERTILITY_AGE) / game_config.LIFE_PART
        i = int(age / fertility_life_period) - 1  # -- i is just a support variable
        chance = self.chance + game_config.FERTILITY_CHANCES[i]
        return self.make_decision(chance)

    def get_partner(self):
        chance = 500
        return self.make_decision(chance)

    def choose_new_profession(self):
        chance = 500
        return self.make_decision(chance)

events = Events()