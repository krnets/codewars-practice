# def find_outlier(integers):
#     return (
#         next(v for v in integers if v & 1)
#         if sum(v & 1 for v in integers) == 1
#         else next(v for v in integers if not v & 1)
#     )


def find_outlier(integers):
    parity = int(sum(v & 1 for v in integers[:3]) > 1)
    return next(v for v in integers if v & 1 != parity & 1)
