# def zero(f=None):  return f(0) if f else 0
# def one(f=None):   return f(1) if f else 1
# def two(f=None):   return f(2) if f else 2
# def three(f=None): return f(3) if f else 3
# def four(f=None):  return f(4) if f else 4
# def five(f=None):  return f(5) if f else 5
# def six(f=None):   return f(6) if f else 6
# def seven(f=None): return f(7) if f else 7
# def eight(f=None): return f(8) if f else 8
# def nine(f=None):  return f(9) if f else 9

# def plus(arg):       return lambda x: x + arg
# def minus(arg):      return lambda x: x - arg
# def times(arg):      return lambda x: x * arg
# def divided_by(arg): return lambda x: x // arg


# def identity(x):       return x
# def plus(arg):         return lambda x: x + arg
# def minus(arg):        return lambda x: x - arg
# def times(arg):        return lambda x: x * arg
# def divided_by(arg):   return lambda x: x // arg

# def zero(f=identity):  return f(0)
# def one(f=identity):   return f(1)
# def two(f=identity):   return f(2)
# def three(f=identity): return f(3)
# def four(f=identity):  return f(4)
# def five(f=identity):  return f(5)
# def six(f=identity):   return f(6)
# def seven(f=identity): return f(7)
# def eight(f=identity): return f(8)
# def nine(f=identity):  return f(9)

from operator import add, sub, mul, floordiv

plus, minus, times, divided_by = map(
    lambda f: lambda y: lambda x: f(x, y), (add, sub, mul, floordiv)
)

zero, one, two, three, four, five, six, seven, eight, nine = map(
    lambda x: lambda f=None: f(x) if f else x, range(10)
)