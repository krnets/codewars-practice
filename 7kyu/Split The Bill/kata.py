# def split_the_bill(x):
#     bill_total = sum(x.values())
#     bill_average = bill_total / len(x)
#     res = {}

#     for friend, amount_spent in x.items():
#         res[friend] = round(amount_spent - bill_average, 2)

#     return res


def split_the_bill(x):
    bill_total = sum(x.values())
    bill_average = bill_total / len(x)
    return {friend: round(x[friend] - bill_average, 2) for friend in x}
