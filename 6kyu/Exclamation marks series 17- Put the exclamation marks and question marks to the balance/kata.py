def balance(left, right):
    left_score = sum("  !?".index(c) for c in left)
    right_score = sum("  !?".index(c) for c in right)
    return "Left" if left_score > right_score else "Right" if right_score > left_score else "Balance"