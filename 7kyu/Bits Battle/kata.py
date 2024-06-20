# def bits_battle(numbers):
#     n_odds, n_evens = 0, 0
#     for x in numbers:
#         if x & 1:     n_odds += x.bit_count()
#         elif x != 0: n_evens += f"{x:b}".count("0")
#     return ("odds win" if n_odds > n_evens else "evens win" if n_evens > n_odds else "tie")

# def bits_battle(numbers):
#     n_odds, n_evens = 0, 0
#     for x in numbers:
#         if x & 1:    n_odds += x.bit_count()
#         elif x > 0: n_evens += len(f"{x:b}") - x.bit_count()
#     return "odds win" if n_odds > n_evens else "evens win" if n_evens > n_odds else "tie"


def bits_battle(numbers):
    score = sum(map(int.bit_count, numbers)) - sum(x.bit_length() for x in numbers if not x & 1)
    return ("tie", "odds win", "evens win")[(score > 0) - (score < 0)]
