import re

def gym_slang(phrase):
    slang = (("probably", "prolly"), ("i am", "i'm"), ("instagram", "insta"), 
             ("do not", "don't"), ("going to", "gonna"), ("combination", "combo"))
    for word_from, word_to in slang:
        phrase = re.sub(word_from[1:], word_to[1:], phrase)
    return phrase
