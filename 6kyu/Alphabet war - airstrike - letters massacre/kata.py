import re

# def alphabet_war(fight):
#     left_power = "sbpw"
#     right_power = "zdqm"
#     left_score, right_score = 0, 0
#     pattern = r"(.?\*+.?)"
#     fight = re.sub(pattern, "", fight)

#     for c in fight:
#         if c in left_power:    left_score += left_power.index(c) + 1
#         elif c in right_power: right_score += right_power.index(c) + 1

#     return  "Left side wins!" if left_score > right_score \
#         else "Right side wins!" if right_score > left_score else "Let's fight again!"


def alphabet_war(fight):
    pattern = re.compile(r"(\w)?\*+(\w)?")
    fight_cleaned = pattern.sub("", fight)
    powers = "mqdz*sbpw"
    score = sum(i * fight_cleaned.count(c) for i, c in enumerate(powers, -4))
    return ("Let's fight again!", "Left side wins!", "Right side wins!")[(score > 0) - (score < 0)]
