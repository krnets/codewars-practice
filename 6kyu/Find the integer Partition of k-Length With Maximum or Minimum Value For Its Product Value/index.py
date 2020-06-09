""" 6kyu - Find the integer Partition of k-Length With Maximum or Minimum Value For Its Product Value

Given a certain integer n, n > 0 and a number of partitions, k, k > 0;
we want to know the partition which has the maximum or minimum product of its terms.

The function find_spec_partition(), will receive three arguments, n, k, and a command: 'max' or 'min'

The function should output the partition that has maximum or minimum value product
(it depends on the given command) as an array with its terms in decreasing order.

Let's see some cases (Python and Ruby)

find_spec_partition(10, 4, 'max') == [3, 3, 2, 2]
find_spec_partition(10, 4, 'min') == [7, 1, 1, 1]

and Javascript:

findSpecPartition(10, 4, 'max') == [3, 3, 2, 2]
findSpecPartition(10, 4, 'min') == [7, 1, 1, 1]

The partitions of 10 with 4 terms with their products are:

(4, 3, 2, 1): 24
(4, 2, 2, 2): 32
(6, 2, 1, 1): 12
(3, 3, 3, 1): 27
(4, 4, 1, 1): 16
(5, 2, 2, 1): 20
(7, 1, 1, 1): 7   <------- min. productvalue
(3, 3, 2, 2): 36  <------- max.product value
(5, 3, 1, 1): 15 """

# from operator import mul
# from functools import reduce
# from collections import defaultdict


# def part(n, k):
#     def memoize(f):
#         cache = [[[None] * n for j in range(k)] for i in range(n)]

#         def wrapper(n, k, pre):
#             if cache[n-1][k-1][pre-1] is None:
#                 cache[n-1][k-1][pre-1] = f(n, k, pre)
#             return cache[n-1][k-1][pre-1]
#         return wrapper

#     @memoize
#     def _part(n, k, pre):
#         if n <= 0:
#             return []
#         if k == 1:
#             if n <= pre:
#                 return [(n,)]
#             return []
#         ret = []
#         for i in range(min(pre, n), 0, -1):
#             ret += [(i,) + sub for sub in _part(n-i, k-1, i)]
#         return ret
#     return _part(n, k, n)


# def find_spec_partition(n, k, com):
#     k_size_parts = part(n, k)
#     prods = defaultdict(list)
#     for p in k_size_parts:
#         prods[reduce(mul, p)].append(p)
#     if com == 'max':
#         max_pv = max(prods.keys())
#         return list(prods[max_pv][0])
#     elif com == 'min':
#         min_pv = min(prods.keys())
#         return list(prods[min_pv][0])


def find_spec_partition(n, k, com):
    q, r = divmod(n, k)
    return {'max': [q+1] * r + [q] * (k-r), 'min': [n+1-k] + [1] * (k-1)}[com]


q = find_spec_partition(10, 4, 'max'), [3, 3, 2, 2]
q
q = find_spec_partition(10, 4, 'min'), [7, 1, 1, 1]
q
