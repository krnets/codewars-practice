from itertools import product

adjacent_keys = {"1": "124", "2": "1235", "3": "236", "4": "1457", "5": "24568", "6": "3569", "7": "478", "8": "57890", "9": "689", "0": "80"} 

# def get_pins(observed):
#     adjacents = map(adjacent_keys.get, observed)
#     return [*map("".join, product(*adjacents))]

def get_pins(observed):
    return [*map("".join, product(*map(adjacent_keys.get, observed)))]