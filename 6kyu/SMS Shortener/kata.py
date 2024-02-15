# def shortener(message):
#     words = message.split()

#     while len(words) > 1 and len(s := " ".join(words)) > 160:
#         b = words.pop()
#         a = words.pop()
#         words.append(a + b[0].upper() + b[1:])

#     return words.pop() if len(words) == 1 else s


def shortener(message):
    words = message.split()

    while len(words) > 1 and len(sms := " ".join(words)) > 160:
        second = words.pop()
        first = words.pop()
        words.append(first + second[0].upper() + second[1:])

    return words.pop() if len(words) == 1 else sms
