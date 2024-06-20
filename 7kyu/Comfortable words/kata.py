# def comfortable_word(word):
#     left = {"q", "w", "e", "r", "t", "a", "s", "d", "f", "g", "z", "x", "c", "v", "b"}
#     right = {"y", "u", "i", "o", "p", "h", "j", "k", "l", "n", "m"}
#     flag = (False, True)[word[0] in left]

#     for c in word:
#         if flag and c in left:
#             flag = False
#         elif not flag and c in right:
#             flag = True
#         else:
#             return False
#     return True


def comfortable_word(word):
    left = {"q", "w", "e", "r", "t", "a", "s", "d", "f", "g", "z", "x", "c", "v", "b"}
    right = {"y", "u", "i", "o", "p", "h", "j", "k", "l", "n", "m"}
    flag = (False, True)[word[0] in left]

    for c in word:
        if (flag and c in left) or (not flag and c in right):
            flag = not flag
        else:
            return False
    return True
