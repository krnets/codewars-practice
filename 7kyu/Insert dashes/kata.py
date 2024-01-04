def insert_dash(num):
    nums = [*map(int, str(num))]
    res = str(nums[0])

    for i in range(1, len(nums)):
        if nums[i - 1] % 2 == 1:
            if nums[i] % 2 == 1:
                res += "-" + str(nums[i])
            else:
                res += str(nums[i])
        else:
            res += str(nums[i])

    return res
