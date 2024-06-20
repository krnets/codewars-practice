import re


# def sursurungal(txt):
#     return re.sub(r"(\d+) (\w+)", convert, txt)


# def f(m):
#     number, word = m.groups()
#     if number <= "1":
#         return m.group()
#     word = word[:-1]
#     if number == "2":
#         return "{} bu{}".format(number, word)
#     if int(number) < 10:
#         return "{} {}zo".format(number, word)
#     return "{} ga{}ga".format(number, word)


# def convert(m):
#     number, word = m.groups()
#     word = word[:-1]
#     match int(number):
#         case x if x in (0, 1): return m.group()
#         case 2: return "{} bu{}".format(number, word)
#         case x if x in range(3, 10): return "{} {}zo".format(number, word)
#         case _: return "{} ga{}ga".format(number, word)

# def convert(m):
#     number, word = m.groups()
#     word = word[:-1]
#     match int(number):
#         case x if x in (0, 1): return m.group()
#         case 2: return "{} bu{}".format(number, word)
#         case x if x in range(3, 10): return "{} {}zo".format(number, word)
#         case _: return "{} ga{}ga".format(number, word)


def sursurungal(txt):
    return re.sub(r"(\d+) (\w+)", pluralise, txt)


def pluralise(m):
    number, word = m.groups()
    word = word[:-1]

    match int(number):
        case x if x <= 1:
            return m.group()
        case 2:
            return "{} bu{}".format(number, word)
        case x if x < 10:
            return "{} {}zo".format(number, word)
        case _:
            return "{} ga{}ga".format(number, word)
