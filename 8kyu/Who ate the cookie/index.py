# 8kyu - Who ate the cookie?

""" For this problem you must create a program that says who ate the last cookie. 
If the input is a string then "Zach" ate the cookie. If the input is a float or 
an int then "Monica" ate the cookie. If the input is anything else "the dog" ate the cookie. 
The way to return the statement is: "Who ate the last cookie? It was (name)!"

Ex: Input = "hi" --> Output = "Who ate the last cookie? It was Zach! 
(The reason you return Zach is because the input is a string) """

# def cookie(x):
#     who = {'s': 'Zach', 'b': 'the dog'}.get(str(type(x))[8:9], 'Monica')
#     return f"Who ate the last cookie? It was {who}!"


def cookie(x):
    who = {str: 'Zach', bool: 'the dog'}.get(type(x), 'Monica')
    return f"Who ate the last cookie? It was {who}!"


q = cookie("Ryan")  # "Who ate the last cookie? It was Zach!"
q
q = cookie(2.3)  # "Who ate the last cookie? It was Monica!"
q
q = cookie(26)  # "Who ate the last cookie? It was Monica!"
q
q = cookie(True)  # "Who ate the last cookie? It was the dog!"
q
