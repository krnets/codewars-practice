# 7kyu - Unlucky Days

""" Friday 13th or Black Friday is considered as unlucky day. 
Calculate how many unlucky days are in the given year.

Find the number of Friday 13th in the given year.

Input: Year as an integer.
Output: Number of Black Fridays in the year as an integer.

unluckyDays(2015) == 3
unluckyDays(1986) == 1 """

from datetime import date


# def unlucky_days(year):
#     return sum(1 for i in range(12) if date(year, i+1, 13).weekday() == 4)


# def unlucky_days(year):
#     return sum(date(year, month, 13).weekday() == 4 for month in range(1, 13))


# def unlucky_days(year):
#     ans = 0

#     for month in range(1, 13):
#         if date(year, month, 13).weekday() == 4:
#             ans += 1

#     return ans


# def unlucky_days(year):
#     ans = 0

#     for month in range(1, 13):
#         if date(year, month, 13).strftime('%A') == 'Friday':
#             ans += 1

#     return ans


# def unlucky_days(year):
#     ans = 0

#     for month in range(1, 13):
#         if date(year, month, 13).ctime().startswith('Fri'):
#             ans += 1

#     return ans


def unlucky_days(year):
    return sum(date(year, m, 13).ctime().startswith("Fri") for m in range(1, 13))


q = unlucky_days(2015)  # 3
q
q = unlucky_days(1986)  # 1
q
