def sum_dig_pow(a, b):
    # return [i for i in range(a, b + 1) if is_eureka(i)]
    return [*filter(is_eureka, range(a, b + 1))]


def is_eureka(n):
    return n == sum(int(d) ** i for i, d in enumerate(str(n), 1))
