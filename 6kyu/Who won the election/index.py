""" 6kyu - Who won the election?

In democracy we have a lot of elections. 
For example, we have to vote for a class representative in school, for a new parliament or a new government.

Usually, we vote for a candidate, i.e. a set of eligible candidates is given. 
This is done by casting a ballot into a ballot-box. After that, it must be counted how many ballots (= votes) a candidate got.

A candidate will win this election if he has the absolute majority.

Your Task: Return the name of the winner. If there is no winner, return None.
There are no given candidates. An elector can vote for anyone. 
Each ballot contains only one name and represents one vote for this name. 
A name is an arbitrary string, e.g. "A", "B", or "XJDHD".

There are no spoiled ballots.

The ballot-box is represented by an unsorted list of names. 
Each entry in the list corresponds to one vote for this name. 
You do not know the names in advance (because there are no candidates).

A name wins the election if it gets more than n/2 votes (n = number of all votes, i.e. n is equal to the size of the given list).

#3 votes for "A", 2 votes for "B" -> "A" wins the election
getWinner(["A", "A", "A", "B", "B"]) == "A" #true

#2 votes for "A", 2 votes for "B" -> No winner
getWinner(["A", "A", "B", "B"]) == None #true

#1 vote for each name -> No winner
getWinner(["A", "B", "C", "D"]) == None #true

#3 votes for "A", 2 votes for "B", 1 vote for "C"  
#-> No winner ("A" does not have more than n/2 = 3 votes)
getWinner(["A", "A", "A", "B", "B", "C"]) == None #true

Please keep in mind the list of votes can be large (n <= 1,200,000). 
The given list is immutable, i.e. you cannot modify the list (otherwise this could lead to vote rigging). """

# from collections import Counter, defaultdict

# def get_winner(ballots):
#     votes = defaultdict(list)
#     for k, v in Counter(ballots).items():
#         votes[v].append(k)
#     if len(votes[max(votes)]) == 1 and max(votes) > len(ballots) / 2:
#         return votes[max(votes)][0]

# from collections import Counter

# def get_winner(ballots):
#     winner, votes = Counter(ballots).most_common(1)[0]
#     return winner if votes > len(ballots) / 2 else None

# def get_winner(ballots):
#     for candidate in set(ballots):
#         if ballots.count(candidate) > len(ballots) / 2:
#             return candidate

def get_winner(ballots):
    return next((c for c in set(ballots) if ballots.count(c) / len(ballots) > 0.5), None)


q = get_winner(("A")), "A"
q
q = get_winner(("A", "A", "A", "B", "B", "B", "A")), "A"
q
q = get_winner(("A", "A", "A", "B", "B", "B")), None
q
q = get_winner(("A", "A", "A", "B", "C", "B")), None
q
q = get_winner(("A", "A", "B", "B", "C")), None
q
q = get_winner(['Tetsuya Tsurugi', 'Maria Fleed', 'Maria Fleed', 'Tetsuya Tsurugi', 'Maria Fleed', 'Hikaru Makiba', 'Tetsuya Tsurugi', 'Tetsuya Tsurugi',
                'Tetsuya Tsurugi', 'Duke Fleed', 'Maria Fleed', 'Tetsuya Tsurugi', 'Maria Fleed', 'Hikaru Makiba', 'Maria Fleed', 'Maria Fleed']), None
q
