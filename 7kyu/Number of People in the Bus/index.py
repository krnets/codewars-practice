# def number(bus_stops):
#     passengers = 0

#     for get_on, get_off in bus_stops:
#         passengers += get_on
#         passengers -= get_off

#     return passengers

# from functools import reduce


# def number(bus_stops):
#     return reduce(lambda acc, x: acc + x[0] - x[1], bus_stops, 0)


# def number(bus_stops):
#     return sum(on - off for on, off in bus_stops)


def number(bus_stops):
    on, off = zip(*bus_stops)
    return sum(on) - sum(off)


q = number([[10, 0], [3, 5], [5, 8]])  # 5
q
q = number([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]])  # 17
q
q = number([[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]])  # 21
q
