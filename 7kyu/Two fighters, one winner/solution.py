"""Create a function that returns the name of the winner in a fight between two fighters.

Each fighter takes turns attacking the other and whoever kills the other first is victorious. 
Death is defined as having health <= 0.

Each fighter will be a Fighter object/instance. 

Both health and damagePerAttack (damage_per_attack for python) will be integers larger than 0. 
You can mutate the Fighter objects.

Your function also receives a third argument, a string, with the name of the fighter that attacks first."""


class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self):
        return "Fighter({}, {}, {})".format(
            self.name, self.health, self.damage_per_attack
        )

    __repr__ = __str__


# def declare_winner(fighter1, fighter2, first_attacker):
#     current_attacker = fighter1 if first_attacker == fighter1.name else fighter2
#     current_defender = fighter2 if current_attacker == fighter1 else fighter1

#     while fighter1.health > 0 and fighter2.health > 0:
#         current_defender.health -= current_attacker.damage_per_attack

#         if current_defender.health > 0:
#             current_attacker, current_defender = current_defender, current_attacker

#     return current_attacker.name


# def declare_winner(fighter1, fighter2, first_attacker):
#     attacker, defender = ((fighter1, fighter2) if first_attacker == fighter1.name else (fighter2, fighter1))

#     while attacker.health > 0 and defender.health > 0:
#         defender.health -= attacker.damage_per_attack

#         if defender.health > 0:
#             attacker, defender = defender, attacker

# return attacker.name


def declare_winner(fighter1, fighter2, first_attacker):
    attacker, defender = (fighter1, fighter2) if first_attacker == fighter1.name else (fighter2, fighter1)

    while defender.health > 0:
        defender.health -= attacker.damage_per_attack
        attacker, defender = defender, attacker

    return attacker.name


q = declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew")  # "Lew"
q
q = declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Harry")  #"Harry"
q
q = declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harry")  #"Harald"
q
q = declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harald")  # "Harald"
q
q = declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Jerry")  # "Harald"
q
q = declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Harald")  # "Harald"
q
