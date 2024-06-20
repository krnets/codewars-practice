# def are_equally_strong(your_left, your_right, friends_left, friends_right):
#     return max(your_left, your_right) == max(friends_left, friends_right) \
#         and min(your_left, your_right) == min(friends_left, friends_right)


def are_equally_strong(your_left, your_right, friends_left, friends_right):
    return {your_left, your_right} == {friends_left, friends_right}
