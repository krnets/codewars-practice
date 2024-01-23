# def determine_time(arr):
#     seconds_in_hour = 60 * 60
#     total_seconds = sum(
#         hh * seconds_in_hour + mm * 60 + ss
#         for hh, mm, ss in (map(int, time.split(":")) for time in arr)
#     )
#     return total_seconds <= seconds_in_hour * 24

from datetime import datetime


def determine_time(arr):
    return sum(d.hour * 60 + d.minute 
               for d in map(lambda x: datetime.strptime(x, "%H:%M:%S"), arr)) <= 24 * 60
