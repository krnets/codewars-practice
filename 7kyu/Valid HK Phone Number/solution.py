import re


# def is_valid_HK_phone_number(number):
#     pattern = r"^\d{4}\s\d{4}$"
#     result = re.search(pattern, number)
#     return result is not None and result.end() == 9


# def has_valid_HK_phone_number(number):
#     pattern = r"\d{4}\s\d{4}"
#     return re.search(pattern, number) is not None

IS_VALID = re.compile(r"^\d{4}\s\d{4}$")
HAS_VALID = re.compile(r"\d{4}\s\d{4}")


def is_valid_HK_phone_number(number):
    return bool(IS_VALID.fullmatch(number, 0, 9))


def has_valid_HK_phone_number(number):
    return bool(HAS_VALID.search(number))
