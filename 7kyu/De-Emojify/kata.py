emojis_idx = { ":)": "0", ":D": "1", ">(": "2", ">:C": "3", ":/": "4", ":|": "5", ":O": "6", ";)": "7", "^.^": "8", ":(": "9", }

# def deemojify(emote_string):
#     chain = []

#     for s in emote_string.split("  "):
#         c = "".join(emap.get(c) for c in s.split())
#         chain.append(chr(int(c)))
#     return "".join(chain)


def deemojify(emote_string):
    chars = []

    for s in emote_string.split("  "):
        c = "".join(map(emojis_idx.get, s.split()))
        chars.append(chr(int(c)))
    return "".join(chars)
