from collections import deque

def sequence_gen(*nums):
    q = deque(nums)
    while True:
        q.append(sum(q))
        yield q.popleft()
