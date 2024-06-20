# def binary_fingers(bin_string):
#     fingers = ["Pinkie", "Ring", "Middle", "Index", "Thumb"]
#     return [x for i, x in enumerate(fingers) if bin_string.rjust(5, "0")[i] == "1"]


def binary_fingers(bin_string):
    fingers = ["Pinkie", "Ring", "Middle", "Index", "Thumb"]
    return [f for f, b in zip(fingers, bin_string.zfill(5)) if b == "1"]