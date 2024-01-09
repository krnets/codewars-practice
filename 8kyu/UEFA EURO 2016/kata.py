# def uefa_euro_2016(teams, scores):
#     ans = f"At match {teams[0]} - {teams[1]}, "

#     if scores[0] > scores[1]:
#         ans += f"{teams[0]} won!"
#     elif scores[0] < scores[1]:
#         ans += f"{teams[1]} won!"
#     else:
#         ans += "teams played draw."

#     return ans

def uefa_euro_2016(teams, scores):
    s1, s2 = scores
    result = "teams played draw." if s1 == s2 else f"{teams[s1 < s2]} won!"
    return f"At match {teams[0]} - {teams[1]}, {result}"

