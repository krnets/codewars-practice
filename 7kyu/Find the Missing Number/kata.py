def missing_no(nums):  # O(n) time | O(1) space
    n = 100
    return n * (n + 1) // 2 - sum(nums)
