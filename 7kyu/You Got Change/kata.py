def give_change(amount):
    denominations = [100, 50, 20, 10, 5, 1]
    res = []

    for denom in denominations:
        n_bills, amount = divmod(amount, denom)
        res.append(n_bills)

    return tuple(res[::-1])
