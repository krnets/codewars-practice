""" 7kyu - Scrabble Score

Write a program that, given a word, computes the scrabble score for that word.
Letter Values

You'll need these:

Letter                           Value
A, E, I, O, U, L, N, R, S, T       1
D, G                               2
B, C, M, P                         3
F, H, V, W, Y                      4
K                                  5
J, X                               8
Q, Z                               10

There will be preloaded a dictionary dict_scores with all these values in your kata. dict_scores["E"] => 1

Examples

"cabbage" --> 14
"cabbage" should be scored as worth 14 points:

    3 points for C
    1 point for A, twice
    3 points for B, twice
    2 points for G
    1 point for E

And to total:

3 + 2*1 + 2*3 + 2 + 1 = 3 + 2 + 6 + 3 = 14

Empty string should return 0. The string can contain spaces and letters (upper and lower case), 
you should calculate the scrabble score only of the letters in that string.

""           --> 0
"STREET"    --> 6
"st re et"    --> 6
"ca bba g  e" --> 14 """

POINTS = {
    1: 'AEIOULNRST',
    2: 'DG',
    3: 'BCMP',
    4: 'FHVWY',
    5: 'K',
    8: 'JX',
    10: 'QZ'}

LETTER_VALS = {}

for k, v in POINTS.items():
    LETTER_VALS.update({x: k for x in v})

def scrabble_score(st):
    return sum(LETTER_VALS[ch] for ch in st.upper() if ch.isalpha())


q = scrabble_score(""), 0
q
q = scrabble_score('a'), 1
q
q = scrabble_score("street"), 6
q
q = scrabble_score("STREET"), 6
q
q = scrabble_score(' a'), 1
q
q = scrabble_score("st re et"), 6
q
