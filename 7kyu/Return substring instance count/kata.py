import re


# def solution(full_text, search_text):
#     return len(re.findall(search_text, full_text))


def solution(full_text, search_text):
    return full_text.count(search_text)
