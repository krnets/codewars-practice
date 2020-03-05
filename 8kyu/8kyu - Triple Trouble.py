# 8kyu - Triple Trouble

""" Create a function that will return a string that combines all of the letters of the three inputed strings in groups. 
Taking the first letter of all of the inputs and grouping them next to each other. Do this for every letter, see example below!

Ex) Input: "aa", "bb" , "cc" => Output: "abcabc"

Note: You can expect all of the inputs to be the same length. """

# from functools import reduce

# def triple_trouble(one, two, three):
#     return ''.join(reduce(lambda x, y: x + y, map(lambda x: list(x), (zip(one, two, three)))))

# def triple_trouble(one, two, three):
#     return ''.join([''.join(x) for x in list(zip(one, two, three))])

# def triple_trouble(one, two, three):
#     return ''.join([a+b+c for a, b, c in zip(one, two, three)])

# def triple_trouble(*args):
#     return ''.join(''.join(a) for a in zip(*args))

def triple_trouble(*args):
    return ''.join(sum(zip(*args), ()))


q = triple_trouble("aaa", "bbb", "ccc")  # "abcabcabc"
q
q = triple_trouble("aaaaaa", "bbbbbb", "cccccc")  # "abcabcabcabcabcabc"
q
q = triple_trouble("burn", "reds", "roll")  # "brrueordlnsl"
q
q = triple_trouble("Bm", "aa", "tn")  # "Batman"
q
q = triple_trouble("LLh", "euo", "xtr")  # "LexLuthor"
q
