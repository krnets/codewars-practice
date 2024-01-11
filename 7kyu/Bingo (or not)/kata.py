# def bingo(array):
#     letters_to_match = set("BINGO")
#     offset = ord("A") - 1
#     chars = [chr(c + offset) for c in array]
#     return ["LOSE", "WIN"][letters_to_match.issubset(chars)]


def bingo(array):
    offset = ord("A") - 1
    letters_to_match = set(ord(c) - offset for c in "BINGO")
    return ["LOSE", "WIN"][letters_to_match.issubset(array)]
