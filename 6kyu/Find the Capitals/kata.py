# def capital(capitals):
#     res = []

#     for d in capitals:
#         country_or_state = d["state"] if "state" in d else d["country"]
#         res.append(f"The capital of {country_or_state} is {d['capital']}")

#     return res


# def capital(capitals):
#     return [
#         f"The capital of {d.get('state') or d['country']} is {d['capital']}"
#         for d in capitals
#     ]


def capital(capitals):
    return ["The capital of {} is {}".format(*entry.values()) for entry in capitals]
