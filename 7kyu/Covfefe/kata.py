# def covfefe(s):
#     return s.replace("coverage", "covfefe") if "coverage" in s else s + " covfefe"


# def covfefe(s):
#     word = "covfefe"
#     return (s + " " + word, s.replace("coverage", word))["coverage" in s]
# word = .__name__
# import sys


def covfefe(s):
    word = "coverage"
    meme = __import__("sys")._getframe().f_code.co_name
    return (s + " " + meme, s.replace(word, meme))[word in s]
