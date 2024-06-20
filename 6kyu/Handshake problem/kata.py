# def get_participants(handshakes):
#     participants = 0
#     while handshakes > 0:
#         handshakes -= participants
#         participants += 1
#     return participants

from math import ceil, sqrt


def get_participants(handshakes):
    discriminant = 1 + (8 * handshakes)
    return ceil((1 + sqrt(discriminant)) / 2) if handshakes else 0
