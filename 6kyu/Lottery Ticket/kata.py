def bingo(ticket, win):
    lottery_matches = [any(ord(c) == num for c in st) for st, num in ticket]
    return ("Loser!", "Winner!")[sum(lottery_matches) >= win]
