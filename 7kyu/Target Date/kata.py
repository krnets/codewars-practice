import datetime as dt
from math import ceil, log

# def date_nb_days(a0, a, p):
#     days = 0
#     p_daily = 1 + p / 100 / 360
#     while a0 < a:
#         a0 *= p_daily
#         days += 1
#     return (dt.date(2016, 1, 1) + dt.timedelta(days)).isoformat()


# def date_nb_days(a0, a, p):
#     daily_interest = 1 + p / 100 / 360
#     days = log(a, daily_interest) - log(a0, daily_interest)
#     return (dt.date(2016, 1, 1) + dt.timedelta(ceil(days))).isoformat()


def date_nb_days(a0, a, p):
    daily_interest = 1 + p / 100 / 360
    days = log(a / a0, daily_interest)
    return (dt.date(2016, 1, 1) + dt.timedelta(ceil(days))).isoformat()
