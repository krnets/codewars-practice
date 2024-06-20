# def encode(s):
#     return " ".join(word[:-1][::-1] + word[-1] for word in s.split())


def encode(s):
    return " ".join(word[-2::-1] + word[-1] for word in s.split())
