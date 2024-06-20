import re


# def get_order(order):
#     menu_items = {"burger": 1, "fries": 2, "chicken": 3, "pizza": 4, "sandwich": 5, "onionrings": 6, "milkshake": 7, "coke": 8 }
#     pattern = "|".join(menu_items.keys())
#     return " ".join(item.title() for item in sorted(re.findall(pattern, order), key=menu_items.get))


# "burger|fries|chicken|pizza|sandwich|onionrings|milkshake|coke"

# def get_order(order):
#     menu_items = { "burger": 1, "fries": 2, "chicken": 3, "pizza": 4, "sandwich": 5, "onionrings": 6, "milkshake": 7, "coke": 8 }
#     pattern = "|".join(menu_items.keys())
#     return " ".join(map(str.title, sorted(re.findall(pattern, order), key=menu_items.get)))

menu_items = { k: v for k, v in zip(["burger", "fries", "chicken", "pizza", "sandwich", "onionrings", "milkshake", "coke"], range(8)) }
re_pattern = "|".join(menu_items.keys())

def get_order(order):
    return " ".join(map(str.title, sorted(re.findall(re_pattern, order), key=menu_items.get)))
