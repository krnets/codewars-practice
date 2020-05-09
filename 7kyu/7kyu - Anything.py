# 7kyu - Anything

""" What is the answer to life the universe and everything

Create a function that will make anything true

    anything({}) != [],          'True'
    anything('Hello') < 'World', 'True'
    anything(80) > 81,           'True'
    anything(re) >= re,          'True'
    anything(re) <= math,        'True'
    anything(5) == ord,          'True' """


import re
import math


# class anything:
#     def __init__(self, thing):
#         self.thing = thing

#     def __eq__(self, value):
#         return True

#     def __ne__(self, value):
#         return True

#     def __le__(self, value):
#         return True

#     def __lt__(self, value):
#         return True

#     def __gt__(self, value):
#         return True

#     def __ge__(self, value):
#         return True

# class anything(object):
#     def __init__(self, thing): pass
#     def __eq__(self, value): return True
#     __ne__ = __lt__ = __gt__ = __ge__ = __le__ = __eq__

class anything:
    def __init__(self, value): pass
    def __eq__(self, other): return True
    __ne__ = __lt__ = __gt__ = __ge__ = __le__ = __eq__


# Anything can be true
# A Dictionary can not equal to a List
q = anything({}) != []
q
# The String Hello can be less than the String world
q = anything('Hello') < 'World'
q
# 80 can be greater than 81
q = anything(80) > 81
q
# A module re can be greater than re
q = anything(re) >= re
q
# A module re can be less than or equal to the module math
q = anything(re) <= math
q
# A number such as 5 can be equal to an undefined variable ord
q = anything(5) == ord
q
