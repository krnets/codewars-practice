# def rpsls(pl1, pl2):
#     rules = { "scissors": "paper", "paper": "rock", "rock": "lizard", "lizard": "spock",
#         "spock": "scissors", "scissors": "lizard", "lizard": "paper",
#         "paper": "spock", "spock": "rock", "rock": "scissors" }
#     n1_steps, n2_steps = 0, 0
#     curr1, curr2 = pl1, pl2

#     while rules[curr1] != pl2:
#         curr1 = rules[curr1]
#         n1_steps += 1

#     while rules[curr2] != pl1:
#         curr2 = rules[curr2]
#         n2_steps += 1
#     return {-1: "Player 1 Won!", 1: "Player 2 Won!"}.get((n2_steps < n1_steps) - (n1_steps < n2_steps), "Draw!")


def rpsls(pl1, pl2):
    rules = {
        "scissors": ["paper", "lizard"],
        "paper": ["rock", "spock"],
        "rock": ["lizard", "scissors"],
        "lizard": ["spock", "paper"],
        "spock": ["scissors", "rock"],
    }
    return {-1: "Player 1 Won!", 1: "Player 2 Won!"}.get((pl1 in rules[pl2]) - (pl2 in rules[pl1]), "Draw!")