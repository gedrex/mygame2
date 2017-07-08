#!/usr/bin/python3
import game_config as config
"""
Industry etc., industry evolution tree
######################################

Agriculture (group Agriculture, produces Basic Food)
 |
 |--Handworking (group Handworking, produces Basic Tools. For evolution needs: [Agriculture, Efectivity 5, Stock 1000])
 |  |
 |--|--Arable farming (group Agriculture, produces Basic floral food, evolution needs: [ [Agriculture, 10, 5000], [Handworking, 5, 2000] ])
 |  |
 |--|--Animal husbandry (group Agriculture, produces Meat, evolution needs: [ [Agriculture, 10, 5000], [Handworking, 5, 2000] ]
"""
BRANCHES_LIST = []  # list of all branches and it's attributes

EVOLVED = []  # list of already discovered branches

class Industry(object):
    """ Definition of branches """
    def __init__(self):
        pass

    def set_initial_attributes(self, name, attributes):
        """set attributes to industry branches
        
        :param name: <string> 
        :param attributes: <dict> 
        """
        self.name = name
        for key, value in attributes.items():
            self.__setattr__(key, value)
        BRANCHES_LIST.append(self)
        if self.name == "Agriculture":
            EVOLVED.append(self)

    def evolve(self):
        EVOLVED.append(self)

    def check_for_evolution(self):
        ready_to_evolve = 0
        for need in self.evolution:
            for evolved_branch in EVOLVED:
                if (evolved_branch.name == need[0]) & (need[1] <= evolved_branch.efectivity) & (need[2] <= evolved_branch.stock):
                    ready_to_evolve += 1
        if ready_to_evolve == len(self.evolution):
            return True

    def manipulate_efectivity(self, efectivity):
        self.efectivity += efectivity

    def manipulate_stock(self, stock):
        self.stock += stock

    def produce(self, human_efectivity):
        ammount_of_produced = human_efectivity * self.efectivity
        self.manipulate_stock(ammount_of_produced)

    def consume(self):
        for consume_item in self.consumption:
            for evolved_branch in EVOLVED:
                if evolved_branch.name == consume_item[0]:
                    evolved_branch.manipulate_stock(-consume_item[1])

    def __repr__(self):
        return '{name}'.format(name=self.__hash__())

