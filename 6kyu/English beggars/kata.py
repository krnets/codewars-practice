def beggars(values, n):
    if not n:
        return []
    queues = [0] * n
    for i, x in enumerate(values):
        queues[i % n] += x
    return queues
