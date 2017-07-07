#!/usr/bin/python3
import game_config
from random import randrange
"""
Human being class and it's attributes and mechanics
"""


class Human(object):
    def __init__(self):
        self.age = 0
        self.max_age = game_config.MAX_HUMAN_AGE  # -- <int> get the max age human can live up to
        self.sex = randrange(2)  # -- <int> get random gender. 0 - Male, 1 - Female
        if self.sex == 0:  # -- <string> Choose randomly from male names list
            self.name = game_config.MALE_NAMES[randrange(len(game_config.MALE_NAMES))]
        else:  # -- <string> Choose randomly from female names list
            self.name = game_config.FEMALE_NAMES[randrange(len(game_config.FEMALE_NAMES))]
        self.profession = game_config.BASIC_PROFESIIONS[0]  # -- set basic profession to Agriculture
        self.parents = []  # -- <list of 2 objects> every human has 2 parents but the first generation
        self.siblings = []  # -- <list of objects> list of objects with same parents
        self.partner = None  # -- <object> almost every human can get some partner at the fertility age

    def choose_partner(self, partners):
        """Choose from list of human objects 
        
        :param partners: <list of objects> -- appropriate human objects
        :return: <object> choosed partner
        """
        appropriate_partners = []
        for potential_partner in partners:
            if (potential_partner.sex != self.sex) & (potential_partner.partner is None) & (potential_partner.age >= game_config.FERTILITY_AGE) & (potential_partner not in self.siblings) & (potential_partner not in self.parents):
                appropriate_partners.append(potential_partner)
        if len(appropriate_partners) > 0:
            return appropriate_partners[randrange(len(appropriate_partners))]

    def die(self):
        """Human die - remove self object"""
        if self.partner is not None:
            self.partner.partner = None
        del self

    def __repr__(self):
        return '{name}'.format(name=self.name)

human = Human()
for key, val in human.__dict__.items():
    print(key, val)
