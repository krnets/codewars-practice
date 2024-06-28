import codewars_test as test
from heapq import heapify, heappop, heappush, heapreplace


# def queue_time(customers, n):
#     tills = [0] * n
#     heapify(tills)

#     for c_time in customers:
#         shortest_till = heappop(tills)
#         heappush(tills, shortest_till + c_time)

#     return max(tills)


# def queue_time(customers, n):
#     tills = [0] * n

#     for c_time in customers:
#         shortest_till_idx = tills.index(min(tills))
#         tills[shortest_till_idx] += c_time

#     return max(tills)


def queue_time(customers, n):
    tills = [0] * n
    heapify(tills)

    for c_time in customers:
        heapreplace(tills, tills[0] + c_time)

    return max(tills)
