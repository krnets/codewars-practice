# def title_case(title, minor_words=""):
#     always_lower_except_first = set(minor_words.lower().split())
#     return " ".join(
#         word.title()
#         if i == 0 or word.lower() not in always_lower_except_first
#         else word.lower()
#         for i, word in enumerate(title.split()))


def title_case(title, minor_words=""):
    minor_set = set(minor_words.lower().split())
    first, *words = title.lower().split(" ")
    words = [w if w in minor_set else w.title() for w in words]
    return " ".join((first.title(), *words))
