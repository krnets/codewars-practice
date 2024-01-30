import calendar as cal

def task(weekday, n_trees, cost_liquid):
    idx = [*cal.day_name].index(weekday)
    name = ("James", "John", "Robert", "Michael", "William")[idx]
    return f"It is {weekday} today, {name}, you have to work, you must spray {n_trees} trees and you need {n_trees * cost_liquid} dollars to buy liquid"