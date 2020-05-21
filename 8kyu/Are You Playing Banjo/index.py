# 8kyu - Are You Playing Banjo?

""" Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

name + " plays banjo" 
name + " does not play banjo"

Names given are always valid strings.  """


# def areYouPlayingBanjo(name):
#     return name + " plays banjo" if name[0].upper() == 'R' else name + " does not play banjo"

def areYouPlayingBanjo(name):
    return name + (' plays' if name[0].upper() == 'R' else ' does not play') + ' banjo'


q = areYouPlayingBanjo("martin")  # "martin does not play banjo"
q
q = areYouPlayingBanjo("Rikke")  # "Rikke plays banjo"
q
