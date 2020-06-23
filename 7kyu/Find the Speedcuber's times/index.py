""" 7kyu - Find the Speedcuber's times!

Speedcubing is the hobby involving solving a variety of twisty puzzles, 
the most famous being the 3x3x3 puzzle or Rubik's Cube, as quickly as possible.

In the majority of Speedcubing competitions, a Cuber solves a scrambled cube 5 times, 
and their result is found by taking the average of the middle 3 solves 
(ie. the slowest and fastest times are disregarded, and an average is taken of the remaining times).

In some competitions, the unlikely event of a tie situation is resolved by comparing Cuber's fastest times.

Write a function cube_times(times) that, given an array of floats times returns an array / tuple 
with the Cuber's result (to 2 decimal places) AND their fastest solve.

For example:

cube_times([9.5, 7.6, 11.4, 10.5, 8.1]) = (9.37, 7.6)
# Because (9.5 + 10.5 + 8.1) / 3 = 9.37 and 7.6 was the fastest solve.

Note: times will always be a valid array of 5 positive floats (representing seconds) """

# from functools import reduce
# from operator import add

# def cube_times(times):
#     arr = sorted(times)
#     return round(reduce(add, arr[1:-1]) / 3, 2), arr[0]


# def cube_times(times):
#     arr = sorted(times)
#     return round(sum(arr[1:-1]) / 3, 2), arr[0]

# def cube_times(times):
#     return round((sum(times) - (min(times) + max(times))) / 3, 2), min(times)

from statistics import mean

def cube_times(times):
    return round(mean(sorted(times)[1:-1]), 2), min(times)


q = cube_times([9.5, 7.6, 11.4, 10.5, 8.1]), (9.37, 7.6)
q
q = cube_times([13.4, 12.3, 9.5, 11.9, 20.8]), (12.53, 9.5)
q
q = cube_times([28.3, 14.5, 17.3, 8.9, 10.1]), (13.97, 8.9)
q
