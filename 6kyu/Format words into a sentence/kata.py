# def format_words(words):
#     if words:
#         words = [*filter(None, words)]
#         match len(words):
#             case 1: return words[0]
#             case 2: return " and ".join(words)
#             case _: return ("{}, " * (len(words) - 2) + "{}").format(*words[:-2], " and ".join(words[-2:]))
#     return ""

def format_words(words):
    if words:
        words = [*filter(None, words)]
        match n := len(words):
            case 1: return words[0]
            case 2: return " and ".join(words)
            case _: return ("{}, " * (n - 2) + "{}").format(*words[:-2], " and ".join(words[-2:]))
    return ""

