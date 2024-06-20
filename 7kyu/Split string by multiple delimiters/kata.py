import re


# def multiple_split(string, delimiters=[]):
#     if not string:
#         return []
#     if not delimiters:
#         return [string]
#     pattern = "[{}]".format("\\".join(delimiters))
#     return [x for x in re.sub(pattern, "|", string).split("|") if x]


# def multiple_split(string, delimiters=[]):
#     if not string:
#         return []
#     if not delimiters:
#         return [string]
#     pattern = "[{}]".format("\\".join(delimiters))
#     return [*filter(None, re.split(pattern, string))]


# pattern = "[{}]".format(re.escape("".join(delimiters)))
# pattern = "[%s]" % "\\".join(delimiters)
# pattern = "[%s]" % re.escape("".join(delimiters))


def multiple_split(string, delimiters=[]):
    if not string:
        return []
    if not delimiters:
        return [string]
    pattern = "[%s]" % re.escape(f"{delimiters}")
    return [*filter(None, re.split(pattern, string))]
