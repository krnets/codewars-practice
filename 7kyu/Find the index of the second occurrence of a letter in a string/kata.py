# def second_symbol(s, symbol):
#     first = s.find(symbol)
#     if first < 0:
#         return -1
#     second = s[first + 1 :].find(symbol)
#     if second < 0:
#         return -1
#     return second + first + 1


def second_symbol(s, symbol):
    return s.find(symbol, s.find(symbol) + 1)
