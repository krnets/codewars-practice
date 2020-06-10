""" 7kyu - Back to Basics

Create a program that will return whether an input value is a str, int, float, or bool. Return the name of the value.

    Input = 23 --> Output = int
    Input = 2.3 --> Output = float
    Input = "Hello" --> Output = str
    Input = True --> Output = bool """

# import re

# def types(x):
#     return re.sub(r"<class \'", '', str(type(x)))[:-2]


# def types(x):
#     return type(x).__name__

def types(x):
    return x.__class__.__name__

q = types(10), "int"
q
q = types(9.7), "float"
q
q = types("Hello"), "str"
q
q = types(True), "bool"
q
