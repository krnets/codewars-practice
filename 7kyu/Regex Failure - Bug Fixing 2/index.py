""" 7kyu - Regex Failure - Bug Fixing #2

Oh no, Timmy's received some hate mail recently but he knows better. 
Help Timmy fix his regex filter so he can be awesome again!  """

import re

def filter_words(phrase):
    return re.sub(r"(?i)bad|mean|ugly|horrible|hideous", 'awesome', phrase)

# def filter_words(phrase):
#     return re.sub(r"bad|mean|ugly|horrible|hideous", 'awesome', phrase, flags=re.I)

q = filter_words("You're Bad! timmy!"), "You're awesome! timmy!"
q
q = filter_words("You're MEAN! timmy!"), "You're awesome! timmy!"
q
