# def repeat_sequence_len(n):
#     seq = [sum_square_digits(n)]
#     repeated_value = 0

#     for i in range(30):
#         curr = sum_square_digits(seq[i])
#         if curr in seq:
#             repeated_value = curr
#             break
#         seq.append(curr)

#     return len(seq) - seq.index(repeated_value)


# def sum_square_digits(n):
#     return sum(int(x) ** 2 for x in str(n))


def repeat_sequence_len(n):
    tortoise = n
    f = lambda m: sum(int(c) ** 2 for c in str(m))
    hare = f(n)
    ans = 1

    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(f(hare))

    hare = f(hare)

    while tortoise != hare:
        hare = f(hare)
        ans += 1

    return ans
