# def bouncing_ball(h, bounce, window):
#     if h <= 0 or bounce < 0 or bounce >= 1 or window >= h:
#         return -1
#     count = 0
#     while h > window:
#         h *= bounce
#         count += 2
#     return count - 1


def bouncing_ball(h, bounce, window):
    if window >= h or bounce < 0 or bounce >= 1:
        return -1
    return 2 + bouncing_ball(h * bounce, bounce, window)
