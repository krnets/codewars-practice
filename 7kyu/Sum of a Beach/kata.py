import re


# def sum_of_a_beach(beach):
#     words = r"sand|water|fish|sun"
#     return len(re.findall(pattern=words, string=beach.lower()))


def sum_of_a_beach(beach):
    words = r"Sand|Water|Fish|Sun"
    return len(re.findall(pattern=words, string=beach, flags=re.IGNORECASE))
