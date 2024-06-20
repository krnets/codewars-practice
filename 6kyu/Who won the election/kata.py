from collections import Counter

# def get_winner(ballots):
#     freq = Counter(ballots)
#     most = max(freq.values())
#     if most > len(ballots) / 2:
#         return next(k for k, v in freq.items() if v == most)


def get_winner(ballots):
    winner, n_votes = Counter(ballots).most_common()[0]
    return (None, winner)[n_votes > len(ballots) / 2]