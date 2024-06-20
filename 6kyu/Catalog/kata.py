import re

# def catalog(s, article):
#     res = []
#     pattern = re.compile(r"<prod><name>(.*)</name><prx>(.*)</prx><qty>(\d+)</qty></prod>")

#     for item in s.splitlines():
#         if article in item:
#             name, prx, qty = re.findall(pattern, item)[0]
#             res.append(f"{name} > prx: ${prx} qty: {qty}")
#     return "\r\n".join(res) if res else "Nothing"


def catalog(s, article):
    pattern = re.compile(r"<prod><name>(.*)</name><prx>(.*)</prx><qty>(\d+)</qty></prod>")

    arr = [f"{name} > prx: ${prx} qty: {qty}"
           for name, prx, qty in re.findall(pattern, s)
           if article in name]

    return "\r\n".join(arr) if arr else "Nothing"
