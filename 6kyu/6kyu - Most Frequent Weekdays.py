# 6kyu - Most Frequent Weekdays

""" What is your favourite day of the week? Check if it's the most frequent day of the week in the year.

You are given a year as integer (e. g. 2001). You should return the most frequent day(s) of the week in that year. 
The result has to be a list of days sorted by the order of days in week 
(e. g. ['Monday', 'Tuesday'], ['Saturday', 'Sunday'], ['Monday', 'Sunday']). 
Week starts with Monday.

Input: Year as an int.

Output: The list of most frequent days sorted by the order of days in week (from Monday to Sunday).

Preconditions:

    Week starts on Monday.
    Year is between 1583 and 4000.
    Calendar is Gregorian.

Example:

most_frequent_days(2427) == ['Friday']
most_frequent_days(2185) == ['Saturday']
most_frequent_days(2860) == ['Thursday', 'Friday'] """

# import calendar

# DAYS = 'Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split()

# def most_frequent_days(year):
#     beg = calendar.weekday(year, 1, 1)
#     end = calendar.weekday(year, 12, 31)
#     return DAYS[beg:end+1] if beg <= end else DAYS[:end+1] + DAYS[beg:]


from calendar import weekday, day_name

def most_frequent_days(year):
    beg = weekday(year, 1, 1)
    end = weekday(year, 12, 31)
    return day_name[beg:end+1] if beg <= end else day_name[:end+1] + day_name[beg:]



q = most_frequent_days(2427), ['Friday']
q
q = most_frequent_days(2185), ['Saturday']
q
q = most_frequent_days(1770), ['Monday']
q
q = most_frequent_days(1785), ['Saturday']
q
q = most_frequent_days(1984), ['Monday', 'Sunday']
q
q = most_frequent_days(2000), ['Saturday', 'Sunday']
q
