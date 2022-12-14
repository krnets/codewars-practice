# def my_languages(results):
#     arr = [(name, score) for name, score in results.items() if score >= 60]

#     arr.sort(key=lambda x: x[1], reverse=True)

#     return [name for name, _ in arr]

from operator import itemgetter

# def my_languages(results):
#     return [lang for lang, score in sorted(results.items(), key=itemgetter(1), reverse=True) if score >= 60]

def my_languages(results):
    return sorted((lang for lang, score in results.items() if score >= 60), key=results.get, reverse=True)


q = my_languages({"Java": 10, "Ruby": 80, "Python": 65})  # ["Ruby", "Python"]
q
q = my_languages({"Hindi": 60, "Dutch": 93, "Greek": 71})  # ["Dutch", "Greek", "Hindi"]
q
q = my_languages({"C++": 50, "ASM": 10, "Haskell": 20})  # []
q
