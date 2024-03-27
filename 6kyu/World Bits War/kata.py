# def bits_war(numbers):
#     odds = sum((i.bit_count(), -1 * i.bit_count())[i < 0] for i in numbers if i & 1)
#     even = sum((i.bit_count(), -1 * i.bit_count())[i < 0] for i in numbers if not i & 1)
#     return ("tie", "odds win", "evens win")[(odds > even) - (odds < even)]

# return "evens win" if odds < even else "odds win" if odds > even else "tie"


def bits_war(numbers):
    odds = sum(i.bit_count() * (-1, 1)[i > 0] for i in numbers if i & 1)
    even = sum(i.bit_count() * (-1, 1)[i > 0] for i in numbers if not i & 1)
    return ("tie", "odds win", "evens win")[(odds > even) - (odds < even)]
