from operator import itemgetter


# def find_senior(lst):
#     max_age = max(lst, key=itemgetter("age"))["age"]
# return [dev for dev in lst if dev["age"] == max_age]


def find_senior(lst):
    max_age = max(map(itemgetter("age"), lst))
    return list(filter(lambda dev: dev["age"] == max_age, lst))
