# def queue_time(customers, n):
#     tills = [0] * n

#     for cust in customers:
#         idx = tills.index(min(tills))
#         tills[idx] += cust

#     return max(tills)

import heapq


def queue_time(customers, n):
    tills = [0] * n
    heapq.heapify(tills)

    for customer_time in customers:
        shortest_till = heapq.heappop(tills)
        heapq.heappush(tills, shortest_till + customer_time)

    return max(tills)
