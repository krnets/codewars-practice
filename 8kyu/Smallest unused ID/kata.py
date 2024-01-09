def next_id(arr):
    used_ids = set(arr)

    for i in range(len(arr)):
        if i not in used_ids:
            return i

    return len(arr)