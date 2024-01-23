# def fizz_buzz_cuckoo_clock(time):
#     hour, minute = map(int, time.split(":"))
#     hour = hour % 12 or 12

#     if minute % 3 == 0:
#         if minute % 5 == 0:
#             if minute == 0:
#                 return " ".join(["Cuckoo"] * hour)
#             if minute == 30:
#                 return "Cuckoo"
#             return "Fizz Buzz"
#         return "Fizz"
#     if minute % 5 == 0:
#         return "Buzz"
#     return "tick"


def fizz_buzz_cuckoo_clock(time):
    hh, mm = map(int, time.split(":"))
    hh = hh % 12 or 12
    if mm == 0:      return " ".join(["Cuckoo"] * hh)
    if mm == 30:     return "Cuckoo"
    if mm % 15 == 0: return "Fizz Buzz"
    if mm % 5  == 0: return "Buzz"
    if mm % 3  == 0: return "Fizz"
    return "tick"