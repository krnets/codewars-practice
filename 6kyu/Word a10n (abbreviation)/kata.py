import re

# def abbreviate(s):
#     return re.sub(r"([A-Za-z]+){4,}", lambda m: a10n(m.group(0)), s)

# def a10n(word):
#     return word if (n := len(word)) < 4 else word[0] + str(n - 2) + word[-1]


# def abbreviate(s):
#     return re.sub(r"(?i)([a-z]+){4,}", lambda m: a10n(m.group(0)), s)


# def a10n(word):
#     return word if (n := len(word)) < 4 else word[0] + str(n - 2) + word[-1]


def abbreviate(s):
    return re.sub(r"(?i)([a-z]+){4,}", a10n, s)


def a10n(match):
    a, *mid, b = match.group()
    return "{}{}{}".format(a, len(mid), b)
