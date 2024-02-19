from collections import Counter, defaultdict
import re


# def parse_mana_cost(mana):
#     res = defaultdict(int)
#     if not mana:
#         return res
#     if not re.fullmatch(r"[wubrg\d]+", mana, re.I):
#         return None
#     for v in re.findall(r"\d+|[wubrg]", mana, re.I):
#         if v.isnumeric():
#             if int(v) > 0:
#                 res["*"] = int(v)
#         else:
#             res[v.lower()] += 1
#     return res


def parse_mana_cost(mana):
    if bool(re.fullmatch(r"[wubrg\d]+", mana, re.I)):
        mana_int_to_stars = re.sub(r"\d+", lambda m: "*" * int(m.group()), mana.lower())
        return Counter(mana_int_to_stars)
    return {} if not mana else None
