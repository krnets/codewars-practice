# def bowling_pins(arr: list[int]) -> str:
#     pin_set = [["I"] * i for i in range(1, 5)]
#     counter = 1

#     for i, row in enumerate(pin_set):
#         for j in range(len(row)):
#             if counter in arr:
#                 pin_set[i][j] = "0"
#             counter += 1
#     return "\n".join(" ".join(row).center(7) for row in reversed(pin_set)).replace("0", " ")


# pins = ("{7} {8} {9} {10}", " {4} {5} {6} ", "  {2} {3}  ", "   {1}   ")
# return "\n".join(pins).format(*(("I", " ")[i in arr] for i in range(11)))


def bowling_pins(arr: list[int]) -> str:
    pins = ("   {1}   ", "  {2} {3}  ", " {4} {5} {6} ", "{7} {8} {9} {10}")
    return "\n".join(reversed(pins)).format(*(("I", " ")[i in arr] for i in range(11)))
