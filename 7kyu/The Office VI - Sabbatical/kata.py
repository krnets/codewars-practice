def sabb(s, val, happiness):
    score = val + happiness + sum(1 for c in s if c in set("sabbatical"))
    return "Sabbatical! Boom!" if score > 22 else "Back to your desk, boy."
