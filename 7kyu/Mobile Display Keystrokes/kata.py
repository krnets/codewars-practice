# def mobile_keyboard(s):
#     layout = [ "1", "2abc", "3def", "4ghi", "5jkl", "6mno", "7pqrs", "8tuv", "9wxyz", "*", "0", "#", ]
#     ans = 0
#     for c in s:
#         for key in layout:
#             if c in key:
#                 ans += key.index(c) + 1
#                 break
#     return ans


# def mobile_keyboard(s):
#     layout = "12abc3def4ghi5jkl6mno7pqrs8tuv9wxyz*0#"
#     presses = "11234123412341234123412345123412345111"
#     return sum(map(int, s.translate(str.maketrans(layout, presses))))


# def mobile_keyboard(s):
#     layout = [ "1", "2abc", "3def", "4ghi", "5jkl", "6mno", "7pqrs", "8tuv", "9wxyz", "*", "0", "#" ]
#     presses = "".join("".join([*map(str, range(1, len(key) + 1))]) for key in layout)
#     return sum(map(int, s.translate(str.maketrans("".join(layout), presses))))


# def mobile_keyboard(s):
#     layout = [ "1", "2abc", "3def", "4ghi", "5jkl", "6mno", "7pqrs", "8tuv", "9wxyz", "*", "0", "#" ]
#     presses = "".join("".join(str(i + 1) for i in range(len(key))) for key in layout)
#     return sum(map(int, s.translate(str.maketrans("".join(layout), presses))))


# KEYSTROKES, presses = dict(), ["1234567890*#", "adgjmptw", "behknqux", "cfilorvy", "sz"]
# for i, press in enumerate(presses, 1):
#     KEYSTROKES.update(dict.fromkeys(press, i))

# KEYSTROKES, presses = dict(), ["1234567890*#", "adgjmptw", "behknqux", "cfilorvy", "sz"]
# for i, press in enumerate(presses, 1):
#     KEYSTROKES.update(dict.fromkeys(press, i))

# KEYSTROKES = {
#     dict.fromkeys(key, i)
#     for i, key in enumerate(
#         ["1234567890*#", "adgjmptw", "behknqux", "cfilorvy", "sz"], 1
#     )
# }

layout = [ "1", "2abc", "3def", "4ghi", "5jkl", "6mno", "7pqrs", "8tuv", "9wxyz", "*", "0", "#" ]
KEYSTROKES = {c: i for key in layout for i, c in enumerate(key, 1)}
mobile_keyboard = lambda s: sum(map(KEYSTROKES.get, s))
