# def race(v1, v2, g):
#     if v1 < v2:
#         seconds_in_hour = 60 * 60
#         time_span = g * seconds_in_hour // (v2 - v1)
#         hours = time_span // seconds_in_hour
#         minutes = time_span % seconds_in_hour // 60
#         seconds = time_span % 60
#         return [hours, minutes, seconds]

import datetime as dt


def race(v1, v2, g):
    if v1 < v2:
        d = dt.datetime(1, 1, 1) + dt.timedelta(seconds=3600 * g // (v2 - v1))
        return [d.hour, d.minute, d.second]
