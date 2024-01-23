def find_missing_number(sequence):
    try:
        nums = set(map(int, sequence.split()))
        for i in range(1, len(nums) + 1):
            if i not in nums:
                return i
    except:
        return 1
    return 0
