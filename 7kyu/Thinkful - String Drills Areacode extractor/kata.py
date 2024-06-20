import re

# def area_code(text):
#     return re.findall(r'\((\d{3})\)', text)[0]


def area_code(text):
    return re.search(r"\((\d{3})\)", text).group(1)
