# def cheapest_quote(n):
#     delivery_cost = {40: 3.85, 20: 1.93, 10: 0.97, 5: 0.49, 1: 0.1}
#     ans = 0

#     for bundle_size, bundle_cost in delivery_cost.items():
#         k_bundles = n // bundle_size
#         ans += bundle_cost * k_bundles
#         n -= k_bundles * bundle_size

#     return round(ans, 2)


def cheapest_quote(n):
    delivery_cost = {40: 3.85, 20: 1.93, 10: 0.97, 5: 0.49, 1: 0.1}
    ans = 0

    for bundle_size, bundle_cost in delivery_cost.items():
        ans += n // bundle_size * bundle_cost
        n %= bundle_size

    return round(ans, 2)
