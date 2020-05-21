# 7kyu - Milk and Cookies for Santa

""" Complete the function function that accepts a Date object, 
and returns true if it's Christmas Eve (December 24th), false otherwise. """

from datetime import date

def time_for_milk_and_cookies(dt):
    return dt.month == 12 and dt.day == 24


q = time_for_milk_and_cookies(date(2013, 12, 24))  # True
q
q = time_for_milk_and_cookies(date(2013, 1, 23))   # False
q
q = time_for_milk_and_cookies(date(3000, 12, 24))  # True
q
