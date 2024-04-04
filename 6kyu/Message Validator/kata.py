import re


# def is_a_valid_message(message):
#     if message and (not message[0].isdigit() or message[-1].isdigit()):
#         return False

#     for chunk in re.findall(r"\d+\D+", message):
#         n, chars = re.findall(r"\d+|\D+", chunk)
#         if len(chars) != int(n):
#             return False
#     return True

def is_a_valid_message(message):
    return all(int(n) == len(w) for n, w in re.findall(r"(\d+)([A-Za-z]*)", message))


# def is_a_valid_message(message):
#     return all(int(n) == len(w) for n, w in re.findall(r"(\d+)(\D*)", message))
