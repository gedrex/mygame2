#!/usr/bin/python3
import game_config as config
from industry import EVOLVED
from random import randrange
from possibilities import events
"""
Human being class and it's attributes and mechanics
"""


class Human(object):
    def __init__(self):
        self.age = 0
        self.max_age = config.MAX_HUMAN_AGE  # -- <int> get the max age human can live up to
        self.sex = randrange(2)  # -- <int> get random gender. 0 - Male, 1 - Female
        if self.sex == 0:  # -- <string> Choose randomly from male names list
            self.name = config.MALE_NAMES[randrange(len(config.MALE_NAMES))]
        else:  # -- <string> Choose randomly from female names list
            self.name = config.FEMALE_NAMES[randrange(len(config.FEMALE_NAMES))]
        self.profession = None  # -- set basic profession to Agriculture
        self.parents = []  # -- <list of 2 objects> every human has 2 parents but the first generation
        self.siblings = []  # -- <list of objects> list of objects with same parents
        self.partner = None  # -- <object> almost every human can get some partner at the fertility age
        self.fertility_age = config.FERTILITY_AGE  # -- <int> fertile age starts at... will be changed with evolution
        self.efectivity = 1  # -- <int> how efective is a person
        self.learning_skill = 5  # per how many year man increase efectivity

    def increase_efectivity(self):
        self.efectivity += 1

    def choose_profession(self):
        if self.parents == []:
            self.profession = EVOLVED[0]
        elif events.choose_new_profession():
            return EVOLVED[randrange(len(EVOLVED))]
        else:
            if self.parents[0].efectivity > 2:
                self.__setattr__("efectivity", int(self.parents[0].efectivity/3))
            return self.parents[0].profession

    def choose_partner(self, partners):
        """Choose from list of human objects 
        
        :param partners: <list of objects> -- appropriate human objects
        :return: <object> choosed partner
        """
        appropriate_partners = []
        for potential_partner in partners:
            if (potential_partner.sex != self.sex) & (potential_partner.partner is None) & (potential_partner.age >= config.FERTILITY_AGE) & (potential_partner not in self.siblings) & (potential_partner not in self.parents):
                appropriate_partners.append(potential_partner)
        if len(appropriate_partners) > 0:
            return appropriate_partners[randrange(len(appropriate_partners))]

    def die(self):
        """Human die - remove self object"""
        if self.partner is not None:
            self.partner.partner = None
        del self

    def print_human_attributes(self):
        print(self.__dict__)

    def __repr__(self):
        return '{name}'.format(name=self.name)

human = Human()
for key, val in human.__dict__.items():
    print(key, val)
