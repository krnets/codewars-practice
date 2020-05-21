# 7kyu - Shortest Word

""" Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types. """


# def find_short(s):
#     return min(len(word) for word in s.split())

# def find_short(s):
#     return len(min(s.split(), key=len))

def find_short(s):
    return min(map(len, s.split()))


q = find_short("bitcoin take over the world maybe who knows perhaps")  # 3
q
q = find_short("turns out random q =  than writing out basic ones")  # 3
q
q = find_short("lets talk about javascript the best language")  # 3
q
q = find_short("i want to travel the world writing code one day")  # 1
q
q = find_short("Lets all go on holiday somewhere very cold")  # 2
q
