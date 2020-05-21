# 7kyu - Absent vowel

""" Your job is to figure out the index of which vowel is missing from a given string:

    A has an index of 0,
    E has an index of 1,
    I has an index of 2,
    O has an index of 3,
    U has an index of 4.

There is no need for string validation and every sentence given will contain all vowles but one. 
Also, you won't need to worry about capitals.

"John Doe hs seven red pples under his bsket"          =>  0  ; missing: "a"
"Bb Smith sent us six neatly arranged range bicycles"  =>  3  ; missing: "o" """


# def absent_vowel(x):
#     vowels = 'aeiou'
#     return vowels.index([m for m in vowels if m not in set(c for c in x if c in vowels)][0])

# def absent_vowel(x):
# return ['aeiou'.index(c) for c in 'aeiou' if c not in x][0]

def absent_vowel(x):
    return 'aeiou'.index((set('aeiou') - set(x)).pop())


q = absent_vowel("John Doe hs seven red pples under his bsket")  # 0
q
q = absent_vowel("Bb Smith sent us six neatly arranged range bicycles")  # 3
q
