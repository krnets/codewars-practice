from functools import partial
from operator import attrgetter


class Animal:
    def __init__(self, name, number_of_legs):
        self.name = name
        self.number_of_legs = number_of_legs


# def sort_animals(lst: list[Animal]) -> list[Animal]:
#     return sorted(lst, key=lambda x: (x.number_of_legs, x.name))


# def sort_animals(lst: list[Animal]) -> list[Animal]:
#     return sorted(lst, key=attrgetter("number_of_legs", "name"))

sort_animals = partial(sorted, key=attrgetter("number_of_legs", "name"))
