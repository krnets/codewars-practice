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
#     current_attacker = first_attacker

#     while fighter1.health > 0 and fighter1.health > 0:
#         if current_attacker == fighter1.name:
#             fighter2.health -= fighter1.damage_per_attack
#             current_attacker = fighter2
#         else:
#             fighter1.health -= fighter2.damage_per_attack
#             current_attacker = fighter1

#     return fighter2.name if fighter1.health <= 0 else fighter1.name


def declare_winner(fighter1, fighter2, first_attacker):
    attacker = fighter1 if fighter1.name == first_attacker else fighter2
    defender = fighter2 if attacker.name == fighter1.name else fighter1

    while defender.health > 0:
        defender.health -= attacker.damage_per_attack
        attacker, defender = defender, attacker

    return attacker.name
