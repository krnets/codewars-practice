# 7kyu - Unscrambled eggs

""" Unscramble the eggs.

The string given to your function has had an "egg" inserted directly after each consonant. 
You need to return the string before it became eggcoded.

Example

unscrambleEggs("Beggegeggineggneggeregg"); => "Beginner"
//             "B---eg---in---n---er---"

Kata is supposed to be for beginners to practice regular expressions, so commenting would be appreciated. """

import re

def unscramble_eggs(word):
    # return re.sub('egg', '', word)
    return word.replace('egg', '')


q = unscramble_eggs("ceggodegge heggeregge"), "code here"
q
q = unscramble_eggs("FeggUNegg KeggATeggA"), "FUN KATA"
q
q = unscramble_eggs("Geggoodegg Legguceggkegg!"), 'Good Luck!'
q
