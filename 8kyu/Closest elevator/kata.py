# def elevator(left, right, call):
#     return ("right", "left")[abs(call - left) < abs(call - right)]


def elevator(left, right, call):
    return ("left", "right")[abs(call - left) >= abs(call - right)]
