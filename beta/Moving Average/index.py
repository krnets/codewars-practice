# Beta - Moving Average

""" Given a series of numbers and a fixed subset size, the first element of the moving average 
is obtained by taking the average of the initial fixed subset (n) of the number series. 
Then the subset is modified by "shifting forward"; that is, excluding the first number of the series 
and including the next value in the subset.

Iterate through the list provided, collecting the moving average in a list to be retruned, 
until you reach the final (n) length subset of the list.

The test will be ran on a list of positive intigers with a length > 1. 
For example [0, 1, 2, 3, 4, 44]

If there cannot be an average obtained return None

For more information on moving averages you can read here http://en.wikipedia.org/wiki/Moving_average

result format should be a list of floats ex.

moving_average([40, 30, 50, 46, 39, 44],3) --> [40.0 42.0 45.0 43.0] """


# def moving_average(values, n):
#     if not n: return None
#     averages = []

#     for i in range(len(values)-n+1):
#         window = values[i:i+n]
#         averages.append(sum(window) / n)

#     return averages if averages else None

# def moving_average(values, n):
#     if 0 < n <= len(values):
#         averages = []
#         for i in range(len(values)-n+1):
#             window = values[i:i+n]
#             averages.append(sum(window) / n)
#         return averages

def moving_average(values, n):
    if 0 < n <= len(values):
        return [sum(values[i:i+n]) / n for i in range(len(values)-n+1)]


q = moving_average([40, 30, 50, 46, 39, 44], 3)  # [40.0, 42.0, 45.0, 43.0]
q
q = moving_average([40, 30, 50, 46, 39, 44], 2)
q
#      [35.0, 40.0, 48.0, 42.5, 41.5]
q = moving_average([40, 30, 50, 46, 39, 44], 4)  # [41.5, 41.25, 44.75]
q
q = moving_average([40, 30, 50, 46, 39, 44], 0)  # None
q
