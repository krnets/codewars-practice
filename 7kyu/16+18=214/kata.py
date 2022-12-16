def add(num1, num2):
    nums = []

    while num1 or num2:
        num1, r1 = divmod(num1, 10)
        num2, r2 = divmod(num2, 10)
        nums.append(r1 + r2)

    return int("".join(map(str, reversed(nums)))) if sum(nums) else 0


q = add(2, 11)  # 13
q
q = add(0, 1)  # 1
q
q = add(0, 0)  # 0
q
q = add(16, 18)  # 214
q
q = add(26, 39)  # 515
q
q = add(122, 81)  # 1103
q
q = add(248, 208)  # 4416
q
