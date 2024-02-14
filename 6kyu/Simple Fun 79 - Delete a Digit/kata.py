# def delete_digit(n):
#     digits = list(str(n))
#     nums = [int("".join(digits[:i] + digits[i + 1 :])) for i in range(len(digits))]
#     return max(nums)


def delete_digit(n):
    digits = str(n)
    nums = [digits[:i] + digits[i + 1 :] for i in range(len(digits))]
    return int(max(nums))
