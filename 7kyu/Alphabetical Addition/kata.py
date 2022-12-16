# 7kyu - Alphabetical Addition

""" Your task is to add up letters to one letter.

The function will be given a variable amount of arguments, each one being a letter to add.

    Letters will always be lowercase.
    Letters can overflow (see second to last example of the description)
    If no letters are given, the function should return 'z'  """


# def add_letters(*letters):
#     alpha = [chr(x) for x in range(ord('a'), ord('z')+1)]
#     sum = 25
#     for c in letters:
#         sum += alpha.index(c)+1
#     return alpha[sum % 26]

# from string import ascii_letters

# def add_letters(*letters):
#     idx = sum(map(lambda c: ord(c) - ord("a") + 1, letters)) % 26
#     return ('z' + ascii_letters)[idx]

# from string import ascii_lowercase

# def add_letters(*letters):
#     idx = sum(ascii_lowercase.index(c) + 1 for c in letters) % 26
#     return ascii_lowercase[idx-1]

# def add_letters(*letters):
#     return ascii_lowercase[sum(ascii_lowercase.index(c) + 1 for c in letters) % 26 - 1]

# def add_letters(*letters):
#     return chr(96 + (sum(ord(l) - 96 for l in letters) % 26 or 26))

# def add_letters(*letters):
#     return chr(ord('a') - 1 + (sum(ord(ch) - (ord('a') - 1) for ch in letters) % 26 or 26))

# def add_letters(*letters):
#     return chr(ord('a') + (sum(ord(ch)-ord('a')+1 for ch in letters)-1) % 26)


from string import ascii_lowercase as abc

def add_letters(*letters):
    idx = sum(abc.index(c) + 1 for c in letters) % 26 - 1
    return abc[idx]


q = add_letters("a", "b", "c")  # 'f'
q
q = add_letters("a", "b")  # 'c'
q
q = add_letters("z")  # 'z'
q
q = add_letters("z", "a")  # 'a'
q
q = add_letters("y", "c", "b")  # 'd' # notice the letters overflowing
q
q = add_letters()  # 'z'
q
