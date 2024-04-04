# def middle_me(N, X, Y):
#     return X if N & 1 else (pad := Y * (N // 2)) + X + pad


def middle_me(N, X, Y):
    return (X.center(N + 1, Y), X)[N & 1]
