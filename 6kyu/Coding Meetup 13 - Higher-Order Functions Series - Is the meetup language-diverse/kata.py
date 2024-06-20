# def is_language_diverse(lst):
#     langs = {"Python": 0, "Ruby": 0, "JavaScript": 0}

#     for dev in lst:
#         langs[dev["language"]] += 1

#     return min(langs.values()) > 0 and max(langs.values()) / min(langs.values()) <= 2

from collections import Counter

# def is_language_diverse(lst):
#     langs_count = Counter(map(lambda dev: dev["language"], lst)).values()
#     return max(langs_count) <= 2 * min(langs_count)


def is_language_diverse(lst):
    langs_count = Counter(dev["language"] for dev in lst).values()
    return max(langs_count) <= 2 * min(langs_count)

