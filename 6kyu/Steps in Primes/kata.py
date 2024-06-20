from gmpy2 import is_prime


# def step(g, m, n):
#     return (
#         next(
#             ([i, i + g] for i in range(m, n) if is_prime(i) and is_prime(i + g)),
#             None,
#         )
#         if g <= n - m
#         else None
#     )


def step(g, m, n):
    for i in range(m, n - g):
        if is_prime(i) and is_prime(i + g):
            return [i, i + g]
