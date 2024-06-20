# def find_odd_names(lst):
#     return [dev for dev in lst if sum(map(ord, dev["firstName"])) & 1]

def find_odd_names(lst):
    return [*filter(lambda dev: sum(map(ord, dev["firstName"])) & 1, lst)]