# 8kyu - Century From Year

""" The first century spans from the year 1 up to and including the year 100, 
The second - from the year 101 up to and including the year 200, etc.

Task :

Given a year, return the century it is in.
Input , Output Examples ::

centuryFromYear(1705)  returns (18)
centuryFromYear(1900)  returns (19)
centuryFromYear(1601)  returns (17)
centuryFromYear(2000)  returns (20)  """


# def century(year):
#     return int(year / 100) if year % 100 == 0 else int(year / 100) + 1

# def century(year):
#     return (year + 99) // 100

# def century(year):
#     from math import ceil
#     return ceil(year / 100)

def century(year):
    return 1 + (year - 1) // 100


q = century(1705)  # 18 'Testing for year 1705'
q
q = century(1900)  # 19 'Testing for year 1900'
q
q = century(1601)  # 17 'Testing for year 1601'
q
q = century(2000)  # 20 'Testing for year 2000'
q
q = century(356)  # 4 'Testing for year 356'
q
q = century(89)  # 1 'Testing for year 89'
q
