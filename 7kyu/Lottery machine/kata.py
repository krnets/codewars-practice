import re

# def lottery(s):
#     ans = "".join(dict.fromkeys(re.sub("\D", "", s)).keys())
#     return ans if ans else "One more run!"


def lottery(s):
    return "".join(dict.fromkeys(filter(str.isdigit, s)).keys()) or "One more run!"
