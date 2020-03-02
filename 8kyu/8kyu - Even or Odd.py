# 8kyu - Even or Odd

""" Create a function (or write a script in Shell) that takes an integer 
as an argument and returns "Even" for even numbers or "Odd" for odd numbers. """


def even_or_odd(number):
    return 'Even' if number % 2 == 0 else 'Odd'


q = even_or_odd(2)  # "Even"
q
q = even_or_odd(0)  # "Even"
q
q = even_or_odd(7)  # "Odd"
q
q = even_or_odd(1)  # "Odd"
q
q = even_or_odd(-1)  # "Odd"
q
