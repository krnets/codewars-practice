# 8kyu - Get the mean of an array

""" It's the academic year's end, fateful moment of your school report. The averages must be calculated. 
All the students come to you and entreat you to calculate their average for them. Easy! You just need to write a script.

Return the average of the given array rounded down to its nearest integer.

The array will never be empty. """


# def get_average(marks):
#     from math import floor
#     return floor(sum(marks) / len(marks))

def get_average(marks):
    return sum(marks) // len(marks)

# def get_average(marks):
#     return int(sum(marks) / len(marks))

# def get_average(marks):
#     from math import trunc
#     return trunc(sum(marks) / len(marks))


q = get_average([2, 2, 2, 2])  # 2
q
q = get_average([1, 5, 87, 45, 8, 8])  # 25
q
q = get_average([2, 5, 13, 20, 16, 16, 10])  # 11
q
q = get_average([1, 2, 15, 15, 17, 11, 12, 17, 17,
                 14, 13, 15, 6, 11, 8, 7])  # 11
q
