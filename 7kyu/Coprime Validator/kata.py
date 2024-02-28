def are_coprime(n, m):
    in_common = set(factors(n)).intersection(factors(m))
    return len(in_common) == 1 and in_common.pop() == 1

def factors(n):
    return [x for x in range(1, n // 2 + 1) if n % x == 0] + [n]