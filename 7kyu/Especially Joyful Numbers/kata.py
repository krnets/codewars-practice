# def number_joy(n):
#     m = n
#     digits_sum = 0

#     while m:
#         m, rem = divmod(m, 10)
#         digits_sum += rem

#     return digits_sum * int(str(digits_sum)[::-1]) == n


def number_joy(n):
    digits_sum = sum(map(int, str(n)))
    return digits_sum * int(str(digits_sum)[::-1]) == n
