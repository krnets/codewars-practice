from itertools import zip_longest


# def compare_versions(version1, version2):
#     for a, b in zip_longest(version1.split("."), version2.split(".")):
#         if not a:
#             return False
#         if b:
#             x, y = map(int, (a, b))
#             if x > y:
#                 return True
#             if x < y:
#                 return False
#     return True

# for a, b in zip_longest(*map(lambda x: x.split("."), (version1, version2))):
# for a, b in zip_longest(*map(str.split, (version1, version2))):


def compare_versions(version1, version2):
    a, b = map(lambda x: [*map(int, x.split("."))], (version1, version2))
    return a >= b
