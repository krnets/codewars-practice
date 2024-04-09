# def help_zoom(key):
#     s = "".join(map(str, key))
#     is_palindrome = s == s[::-1]
#     return ("No", "Yes")[is_palindrome]


def help_zoom(key):
    return ("No", "Yes")[key == [*reversed(key)] or 0]
