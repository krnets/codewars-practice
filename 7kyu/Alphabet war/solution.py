# def alphabet_war(fight):
#     left_score = 0
#     right_score = 0
#     left_letter_powers = {"w": 4, "p": 3, "b": 2, "s": 1}
#     right_letter_powers = {"m": 4, "q": 3, "d": 2, "z": 1}

#     for c in fight:
#         if c in left_letter_powers:
#             left_score += left_letter_powers[c]
#         elif c in right_letter_powers:
#             right_score += right_letter_powers[c]

#     if left_score == right_score:
#         return "Let's fight again!"

#     return "Right side wins!" if left_score < right_score else "Left side wins!"


def alphabet_war(fight):
    result = sum("sbpw".find(c) - "zdqm".find(c) for c in fight)

    return (
        f"{'Left' if result > 0 else 'Right'} side wins!"
        if result
        else "Let's fight again!"
    )


q = alphabet_war("z")  # "Right side wins!"
q
q = alphabet_war("zdqmwpbs")  # "Let's fight again!"
q
q = alphabet_war("wq")  # "Left side wins!"
q
q = alphabet_war("zzzzs")  # "Right side wins!"
q
q = alphabet_war("wwwwww")  # "Left side wins!"
q
