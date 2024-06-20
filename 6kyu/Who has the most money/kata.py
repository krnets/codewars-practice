class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties


def most_money(students):
    amounts = { st.name: 5 * st.fives + 10 * st.tens + 20 * st.twenties for st in students }
    return "all" if len(students) > 1 and len(set(amounts.values())) == 1 else max(amounts, key=amounts.get)


# def most_money(students):
#     amounts = [sum([5 * st.fives + 10 * st.tens + 20 * st.twenties]) for st in students]
#     if len(students) > 1 and len(set(amounts)) == 1:
#         return "all"
#     return students[amounts.index(max(amounts))].name
