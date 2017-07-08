#!/usr/bin/python3
import industry
from possibilities import Events
import game_config as config
import man
import time

class Game(object):
    def __init__(self):
        self.game_year = 0
        self.population = []
        for key, value in config.BRANCHES_TREE.items():
            industry.Industry().set_initial_attributes(key, value)
        for i in range(config.STARTING_COUNT_OF_PEOPLE):
            self.population.append(man.Human())

    def life(self):
        for this_person in self.population:

            # clovek zemre
            if Events(this_person.age).death():
                this_person.die()

            # pokud je clovek v plodnem veku, tak:
            if this_person.age >= this_person.fertility_age:
                #pokud nema partnera, bude se ho snazit najit
                if this_person.partner is None:
                    self.try_to_get_partner(this_person)
                else:
                    #pokud je zena, bude se snazit mit potomka
                    if this_person.sex:
                        self.try_to_have_offspring(this_person)
            this_person.age += 1

        print(industry.BRANCHES_LIST)

        self.game_year += 1
        time.sleep(1)

    def industry_evolution(self):
        for branch in industry.BRANCHES_LIST:
            if branch not in industry.EVOLVED:
                if industry.Industry.check_for_evolution(branch):
                    print("Congratulation! You just discovered {name}".format(name=branch.name))
                    industry.Industry.evolve(branch)

    def try_to_get_partner(self, human):
        if Events(human.age).get_partner():
            self.get_partner(human)

    def get_partner(self, human, **kwargs):
        partner = man.Human.choose_partner(human, self.population)
        if partner is not None:
            human.partner = partner
            human.partner.partner = human

    def try_to_have_offspring(self, human):
        if Events(human.age).have_offspring():
            self.have_offspring(human)

    def have_offspring(self, human):
        new_human = man.Human()
        new_human.parents = [human, human.partner]
        new_human.profession = man.Human.choose_profession()
        self.population.append(new_human)

game = Game()


while True:
    game.life()
    for key, val in game.__dict__.items():
        print(key, val)
    print(len(game.population))