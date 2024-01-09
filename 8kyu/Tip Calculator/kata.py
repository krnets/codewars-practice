from math import ceil


def calculate_tip(amount, rating):
    match rating.lower():
        case 'terrible': return 0
        case 'poor': return ceil(amount * .05)
        case 'good': return ceil(amount * .1)
        case 'great': return ceil(amount * .15)
        case 'excellent': return ceil(amount * .2)
        case _: return 'Rating not recognised'