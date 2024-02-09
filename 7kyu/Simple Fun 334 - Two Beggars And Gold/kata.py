# def distribution_of(golds):
#     left, right = 0, len(golds) - 1
#     pile_A, pile_B = 0, 0
#     turn_A = True

#     while left <= right:
#         if golds[left] >= golds[right]:
#             if turn_A:  pile_A += golds[left]
#             else:       pile_B += golds[left]
#             left += 1
#         else:
#             if turn_A:  pile_A += golds[right]
#             else:       pile_B += golds[right]
#             right -= 1
#         turn_A = not turn_A

#     return [pile_A, pile_B]

from collections import deque


def distribution_of(golds):
    turn = 0
    beggars = [0, 0]
    piles = deque(golds)
    while piles:
        beggars[turn] += (piles.popleft, piles.pop)[piles[0] < piles[-1]]()
        turn ^= 1
    return beggars
