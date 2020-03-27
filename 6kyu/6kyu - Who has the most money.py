# 6kyu - Who has the most money?

""" You're going on a trip with some students and it's up to you to keep track of how much money 
each Student has. A student class is pre-defined.

Each Student has some fives, tens, and twenties. 
Your job is to return the name of the student with the most money. 
If every student has the same amount, then return "all".

    Each student will have a unique name
    There will always be a clear winner: either one person has the most, or everyone has the same amount
    If there is only one student, then that student has the most money """


class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties


def most_money(students):
    res = [sum([x.fives * 5, x.tens * 10, x.twenties * 20]) for x in students]
    if len(students) > 1 and all(x == res[0] for x in res):
        return 'all'
    return students[res.index(max(res))].name


phil = Student("Phil", 2, 2, 1)
cam = Student("Cameron", 2, 2, 0)
geoff = Student("Geoff", 0, 3, 0)

q = most_money([cam, geoff, phil])  # "Phil"
q
q = most_money([cam, geoff])  # "all"
q
q = most_money([geoff])  # "Geoff"
q
