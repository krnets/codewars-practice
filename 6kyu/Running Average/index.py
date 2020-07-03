""" 6kyu - Running Average

Create a function running_average() that returns a callable function object. 
Update the series with each given value and calculate the current average.

r_avg = running_average()
r_avg(10) = 10.0
r_avg(11) = 10.5
r_avg(12) = 11

All input values are valid. Round to two decimal places.
This Kata is based on a example from Fluent Python book."""

# class running_average():
#     def __init__(self):
#         self.series = []

# def __call__(self, new_value):
#     self.series.append(new_value)
#     total = sum(self.series)
#     return round(total / len(self.series), 2)


# def running_average():
#     data = []
#     def mean(n):
#         data.append(n)
#         return round(sum(data) / len(data), 2)
#     return mean

# def running_average():
#     class Average(object):
#         count = total = 0
#         @staticmethod
#         def __new__(self, x):
#             self.count += 1
#             self.total += x
#             return round(self.total / self.count, 2)
#     return Average

def running_average():
    count = total = 0

    def avg(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return round(total / count, 2)
    return avg


r_avg = running_average()

q = r_avg(10), 10
q
q = r_avg(11), 10.5
q
q = r_avg(12), 11
q
