# def next_happy_year(year):
#     ans = year + 1
#     while len(set(str(ans))) != 4:
#         ans += 1
#     return ans


# def next_happy_year(year):
#     year += 1
#     while len(set(str(year))) != 4:
#         year += 1
#     return year


def next_happy_year(year):
    year += 1
    return year if len(set(str(year))) == 4 else next_happy_year(year)
