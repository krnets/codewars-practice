# def char_concat(word):
#     ans = ""
#     for i in range(len(word) // 2):
#         ans += word[i] + word[-i - 1] + str(i + 1)
#     return ans


# def char_concat(word):
#     return "".join(word[i] + word[-i - 1] + str(i + 1) for i in range(len(word) // 2))


# def char_concat(word):
#     return "".join("{}{}{}".format(word[i], word[-i - 1], i + 1) for i in range(len(word) // 2))


def char_concat(word):
    return "".join("{}{}{}".format(word[i], word[~i], i+1) for i in range(len(word) // 2))
