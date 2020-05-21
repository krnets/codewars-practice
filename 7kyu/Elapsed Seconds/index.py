# 7kyu - Elapsed Seconds

""" Complete the function so that it returns the number of seconds 
that have elapsed between the start and end times given.

    The start/end times are given as datetime(Python) instances.
    The start time will always be before the end time. """

from datetime import datetime

def elapsed_seconds(start, end):
    return (end - start).seconds


start = datetime(2013, 1, 1, 0, 0, 1)
end = datetime(2013, 1, 1, 0, 0, 2)
end2 = datetime(2013, 1, 1, 0, 0, 20)
end3 = datetime(2013, 1, 1, 0, 1, 20)

q = elapsed_seconds(start, end)  # 1
q
q = elapsed_seconds(end, end2)  # 18
q
q = elapsed_seconds(start, end2)  # 19
q
q = elapsed_seconds(start, end3)  # 79
q
q = elapsed_seconds(end, end3)  # 78
q
