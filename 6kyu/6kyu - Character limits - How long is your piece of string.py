# 6kyu - Character limits: How long is your piece of string?

""" Cara is applying for several different jobs. 
The online application forms ask her to respond within a specific character count. 
Cara needs to check that her answers fit into the character limit.

Annoyingly, some application forms count spaces as a character, and some don't.

Your challenge:

Write Cara a function charCheck() with the arguments:

    "text": a string containing Cara's answer for the question
    "max": a number equal to the maximum number of characters allowed in the answer
    "spaces": a boolean which is True if spaces are included in the character count and False if they are not

The function charCheck() should return an array: [True, "Answer"] , 
where "Answer" is equal to the original text, if Cara's answer is short enough.

If her answer "text" is too long, return an array: [False, "Answer"]. 
The second element should be the original "text" string truncated to the length of the limit.

When the "spaces" argument is False, you should remove the spaces from the "Answer".

For example:

    charCheck("Cara Hertz", 10, True) should return [ True, "Cara Hertz" ]
    charCheck("Cara Hertz", 9, False) should return [ True, "CaraHertz" ]
    charCheck("Cara Hertz", 5, True) should return [ False, "Cara " ]
    charCheck("Cara Hertz", 5, False) should return [ False, "CaraH" ] """

# import re

# def charCheck(text, mx, spaces):
#     if not spaces:
#         text = re.sub(r'\s', '', text)
#     return [len(text) <= mx, text[:mx]]

def charCheck(text, mx, spaces):
    text = text if spaces else text.replace(' ', '')
    return [len(text) <= mx, text[:mx]]

# def charCheck(s, mx, spaces):
#     res = ''.join((s.split(), s)[spaces])
#     return [len(res) <= mx, res[:mx]]


# should return OK if texts fit character count
q = charCheck("I am applying for the role of Base Manager on Titan.", 60, True)
q
#      [True, "I am applying for the role of Base Manager on Titan."]

q = charCheck(
    "I am looking to relocate to the vicinity of Saturn for family reasons.", 70, True)
q
#      [True, "I am looking to relocate to the vicinity of Saturn for family reasons."]

# should return true if texts fit character count, with spaces removed if needed
q = charCheck(
    "As Deputy Base Manager on Phobos for five Martian years, I have significant relevant experience.", 90, False)
q
#      [True, "AsDeputyBaseManageronPhobosforfiveMartianyears,Ihavesignificantrelevantexperience."]

q = charCheck(
    "A challenging career moment came with the rapid depletion of water supplies on Phobos.", 80, False)
q
#      [True, "AchallengingcareermomentcamewiththerapiddepletionofwatersuppliesonPhobos."]

# "should not return true if texts do not fit character count, with spaces included if needed
q = charCheck(
    "I swiftly resolved the situation with base-wide water rationing.", 60, True)
q
#      [False, "I swiftly resolved the situation with base-wide water ration"]

q = charCheck(
    "After four Martian weeks of not washing, several colonists complained of the smell.", 80, True)
q
#      [False, "After four Martian weeks of not washing, several colonists complained of the sme"]


# "should return expected array if texts do not fit character count
q = charCheck(
    "But, as I pointed out, anyone complaining about standing downwind was lying. There was no wind.", 75, True)
q
#      [False, "But, as I pointed out, anyone complaining about standing downwind was lying"]

q = charCheck(
    "I have no notice period on Phobos. I can start immediately.", 50, True)
q
#      [False, "I have no notice period on Phobos. I can start imm"]
