# def year_days(year):
#     return "{} has {} days".format(year, (365, 366)[is_leap(year)])

# def is_leap(year):
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

from calendar import isleap

def year_days(year):
    return f"{year} has {365 + isleap(year)} days"
