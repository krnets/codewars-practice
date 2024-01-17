# def scrolling_text(text):
#     text = text.upper()
#     return [text[i:] + text[:i] for i in range(len(text))]

from collections import deque


def scrolling_text(text):
    res = []

    for i in range(len(text)):
        dq = deque(text)
        dq.rotate(-i)
        res.append("".join(dq).upper())

    return res
