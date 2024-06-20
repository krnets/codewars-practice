from gmpy2 import next_prime, is_prime


def backwards_prime(start, stop):
    res = []
    i = start

    while i <= stop:
        i = next_prime(i)
        m = int(str(i)[::-1])

        if is_prime(m) and i <= stop and m != i:
            res.append(i)

    return res
