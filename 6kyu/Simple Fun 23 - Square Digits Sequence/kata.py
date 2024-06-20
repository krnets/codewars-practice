def square_digits_sequence(n):
    nums = set()
    while n not in nums:
        nums.add(n)
        n = sum(x * x for x in map(int, str(n)))
    return len(nums) + 1
