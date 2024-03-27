from math import pi


def iter_pi(epsilon):
    steps, leibniz = 1, 1

    while abs(4 * leibniz - pi) > epsilon:
        m = 1 / (2 * steps + 1)
        if steps & 1:
            leibniz -= m
        else:
            leibniz += m
        steps += 1

    return [steps, round(4 * leibniz, 10)]
