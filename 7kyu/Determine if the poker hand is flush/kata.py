# def is_flush(cards):
#     return len(set(card[-1] for card in cards)) == 1


# The possible card values are
# 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A


# def is_flush(cards):
#     return all(card[-1] == cards[0][-1] for card in cards)

def is_flush(cards):
    return all(card.endswith(cards[0][-1]) for card in cards)
