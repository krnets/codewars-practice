pokemon_matchup = (
    ("electric", "water"),
    ("water", "fire"),
    ("fire", "grass"),
    ("grass", "water"),
)


def calculate_damage(your_type, opponent_type, attack, defense):
    effectiveness = 1
    if your_type == opponent_type or (opponent_type, your_type) in pokemon_matchup:
        effectiveness /= 2
    if (your_type, opponent_type) in pokemon_matchup:
        effectiveness *= 2
    return 50 * (attack / defense) * effectiveness
