def get_score(arr) -> int:
    total, running_sum = 0, 0
    base_scores = [0, 40, 100, 300, 1200]

    for x in arr:
        total += base_scores[x] * (running_sum // 10 + 1)
        running_sum += x

    return total
