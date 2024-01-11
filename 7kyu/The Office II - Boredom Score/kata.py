boredom_assessment_score = { "accounts": 1, "finance": 2, "regulation": 3, "cleaning": 4,
    "trading": 6, "change": 6, "IS": 8, "retail": 5, "canteen": 10, "pissing about": 25, }

def boredom(staff):
    score = sum(map(boredom_assessment_score.get, staff.values()))
    return "party time!!" if score >= 100 else "i can handle this" if score > 80 else "kill me now"