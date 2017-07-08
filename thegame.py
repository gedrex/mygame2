#!/usr/bin/python3
import industry
from possibilities import events
import game_config as config
import man
import time

class Game(object):
    def __init__(self):
        self.game_year = 0
        self.population = []
        self.industry = industry.Industry()
        for key, value in config.BRANCHES_TREE.items():
            industry.Industry().set_initial_attributes(key, value)
        for i in range(config.STARTING_COUNT_OF_PEOPLE):
            new_man = man.Human()
            new_man.choose_profession()
            self.population.append(new_man)

    def life(self):
        for this_person in self.population:

            # clovek zemre
            if events.death(this_person.age):
                this_person.die()

            ### life, love ###
            # pokud je clovek v plodnem veku, tak:
            if this_person.age >= this_person.fertility_age:
                #pokud nema partnera, bude se ho snazit najit
                if this_person.partner is None:
                    self.try_to_get_partner(this_person)
                else:
                    #pokud je zena, bude se snazit mit potomka
                    if this_person.sex:
                        self.try_to_have_offspring(this_person)
            ### professional life ###
            # increase efectivity
            if this_person.age % this_person.learning_skill == 0:
                this_person.increase_efectivity
            # produce product of man's profession
            this_person.profession.produce(this_person.efectivity)
            if len(this_person.profession.consumption) > 0:
                this_person.profession.consume()


            this_person.age += 1

        for branch in industry.BRANCHES_LIST:
            branch.check_for_evolution()

        self.industry_stats = industry.EVOLVED

        self.game_year += 1
        time.sleep(1)

    def industry_evolution(self):
        for branch in industry.BRANCHES_LIST:
            if branch not in industry.EVOLVED:
                if self.industry.check_for_evolution(branch):
                    print("Congratulation! You just discovered {name}".format(name=branch.name))
                    self.industry.evolve(branch)

    def try_to_get_partner(self, human):
        if events.get_partner():
            self.get_partner(human)

    def get_partner(self, human, **kwargs):
        partner = man.Human.choose_partner(human, self.population)
        if partner is not None:
            human.partner = partner
            human.partner.partner = human

    def try_to_have_offspring(self, human):
        if events.have_offspring(human.age):
            self.have_offspring(human)

    def have_offspring(self, human):
        new_human = man.Human()
        new_human.parents = [human, human.partner]
        new_human.profession = new_human.choose_profession()
        self.population.append(new_human)

game = Game()


while True:
    game.life()
    for indy in game.industry_stats:
        print("{name} - {product}: Stock: {stock} Efectivity: {efectivity}".format(name=indy.name, product=indy.product, stock=indy.stock, efectivity=indy.efectivity))