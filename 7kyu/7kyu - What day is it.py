# 7kyu - What day is it?

""" If I give you a date, can you tell me what day that date is? 
For example, december 8th, 2015 is a tuesday.

Your job is to write the function day(d) which takes a string representation of a date as input, 
in the format YYYYMMDD. 
The example would be "20151208". 
The function needs to output the string representation of the day, so in this case "Tuesday".

Your function should be able to handle dates ranging from January first, 1582 
(the year the Gregorian Calendar was introduced) to December 31st, 9999. 
You will not be given invalid dates. Remember to take leap years into account. """

# import datetime

# def day(date):
#     yy = int(date[0:4])
#     mm = int(date[4:6])
#     dd = int(date[6:8])
#     return datetime.date(yy, mm, dd).strftime('%A')

# from calendar import day_name
# from datetime import date as dt

# def day(date):
#     yy = int(date[0:4])
#     mm = int(date[4:6])
#     dd = int(date[6:8])
#     return day_name[dt(yy, mm, dd).weekday()]

# from datetime import strptime
# from datetime import datetime as dt

# def day(date):
#     return '{:%A}'.format(dt.strptime(date, '%Y%m%d'))

from dateutil import parser
from calendar import day_name

def day(date):
    return day_name[parser.parse(date).weekday()]


# Test.describe("Basic Tests")
q = day("20151208")  # "Tuesday", "December 8th, 2015 is a Tuesday."
q
q = day("20140728")  # "Monday", "July 28th, 2014 is a Monday"
q

# Test.describe("Leap year tests")
q = day("20160229")  # "Monday", "February 29th, 2016 is a Monday"
q
q = day("20160301")  # "Tuesday", "March first, 2016 is a Tuesday"
q
q = day("19000228")  # "Wednesday", "February 28th, 1900 is a Wednesday"
q
q = day("19000301")  # "Thursday", "March first, 1900 is a Thursday"
q
