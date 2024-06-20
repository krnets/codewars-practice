from math import sqrt

# def perfect_roots(n):
#     return sqrt(sqrt(sqrt(n))).is_integer()


# def perfect_roots(n):
#     return all(int(n**i) == n**i for i in (0.5, 0.25, 0.125))


# def perfect_roots(n):
#     return all(int(n ** (1 / i)) == n ** (1 / i) for i in (2, 4, 8))


# def perfect_roots(n):
#     return all(int(n ** (1 / i)) == n ** (1 / i) for i in (0b10, 0b100, 0b1000))


def perfect_roots(n):
    return all(int(p := n ** (1 / i)) == p for i in (0b10, 0b100, 0b1000))
