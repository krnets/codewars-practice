# def rank(st, we, n):
#     if not st:
#         return "No participants"
#     offset = ord("A") - 1
#     names = st.split(",")
#     if len(names) < n:
#         return "Not enough participants"
#     arr = [(weight * -(len(name) + (sum(ord(c) - offset for c in name.upper()))), name)
#            for name, weight in zip(names, we)]
#     return sorted(arr)[n - 1][1]


def rank(st, we, n):
    if not st:      return "No participants"
    if len(we) < n: return "Not enough participants"
    offset = ord("A") - 1
    winning_number = lambda name, weight: weight * (len(name) + (sum(ord(c) - offset for c in name.upper())))
    arr = [(-winning_number(name, weight), name) for name, weight in zip(st.split(","), we)]
    return sorted(arr)[n - 1][1]