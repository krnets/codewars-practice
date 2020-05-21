# 8kyu - Calculate average

""" Write function avg which calculates average of numbers in given list.

Python:

    Due to rounding issues please do not use statistics.mean or such.
    If the array is empty, return 0.  """


# def find_average(arr):
#     return sum(arr) / len(arr)

def find_average(arr):
    return sum(arr) / len(arr) if arr else 0


array = [1, 2, 3]
q = find_average(array)  # 2
q
