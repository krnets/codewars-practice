# 8kyu - Return the day

""" Complete the function which returns the weekday according to the input number:

    1 returns "Sunday"
    2 returns "Monday"
    3 returns "Tuesday"
    4 returns "Wednesday"
    5 returns "Thursday"
    6 returns "Friday"
    7 returns "Saturday"
    Otherwise returns "Wrong, please enter a number between 1 and 7" """

# def whatday(num):
#     weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
#     return weekdays[num-1] if num >= 1 and num <= 7 else "Wrong, please enter a number between 1 and 7"


def whatday(num):
    weekdays = " Sunday Monday Tuesday Wednesday Thursday Friday Saturday".split(" ")
    return weekdays[num] if 0 < num <= 7 else "Wrong, please enter a number between 1 and 7"


q = whatday(1)  # 'Sunday'
q
q = whatday(2)  # 'Monday'
q
q = whatday(3)  # 'Tuesday'
q
q = whatday(7)  # 'Saturday'
q
q = whatday(8)  # 'Wrong, please enter a number between 1 and 7'
q
q = whatday(20)  # 'Wrong, please enter a number between 1 and 7'
q
