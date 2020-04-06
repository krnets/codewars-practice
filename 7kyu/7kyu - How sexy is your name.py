# 7kyu - How sexy is your name?

""" How sexy is your name?
Write a program that calculates how sexy one's name is according to the criteria below.

There is a preloaded dictionary of letter scores called SCORES.
Add up the letters (case-insensitive) in your name to get your sexy score.
Ignore other characters.

The program must return how sexy one's name is according to the "Sexy score ranking" chart.

       score <= 60:   'NOT TOO SEXY'
 61 <= score <= 300:  'PRETTY SEXY'
301 <= score <= 599:  'VERY SEXY'
       score >= 600:  'THE ULTIMATE SEXIEST' """

SCORES = {'A': 100, 'B': 14, 'C': 9, 'D': 28, 'E': 145, 'F': 12, 'G': 3,
          'H': 10, 'I': 200, 'J': 100, 'K': 114, 'L': 100, 'M': 25,
          'N': 450, 'O': 80, 'P': 2, 'Q': 12, 'R': 400, 'S': 113, 'T': 405,
          'U': 11, 'V': 10, 'W': 10, 'X': 3, 'Y': 210, 'Z': 23}


# def sexy_name(name):
#     """ calculate the sexy name score and return the sexy score ranking """
#     score = sum(SCORES[x] for x in list(name.upper()) if x.isalpha())
#     if score <= 60:
#         return 'NOT TOO SEXY'
#     elif 61 <= score <= 300:
#         return 'PRETTY SEXY'
#     elif 301 <= score <= 599:
#         return 'VERY SEXY'
#     elif score >= 600:
#         return 'THE ULTIMATE SEXIEST'

# def sexy_name(name):
#     n = sum(SCORES.get(x, 0) for x in name.upper())
#     return ['NOT TOO SEXY',  'PRETTY SEXY', 'VERY SEXY',  'THE ULTIMATE SEXIEST'][sum([n >= 61, n >= 301, n >= 600])]

def sexy_name(name):
    score = sum(SCORES.get(x, 0) for x in name.upper())
    if score >= 600:
        return 'THE ULTIMATE SEXIEST'
    elif score >= 301:
        return 'VERY SEXY'
    elif score >= 61:
        return 'PRETTY SEXY'
    return 'NOT TOO SEXY'


# 'Not too sexy!'
q = sexy_name('GUV')  # 'NOT TOO SEXY'
q
q = sexy_name('PHUG')  # "NOT TOO SEXY"
q
q = sexy_name('FFFFF')  # 'NOT TOO SEXY'
q
q = sexy_name('')  # "NOT TOO SEXY"
q
q = sexy_name('PHUG')  # "NOT TOO SEXY"
q

# 'Pretty sexy!'
q = sexy_name('BOB')  # "PRETTY SEXY"
q
q = sexy_name('JLJ')  # 'PRETTY SEXY'
q
q = sexy_name('HHHHHU')  # 'PRETTY SEXY'
q
q = sexy_name('BOB')  # "PRETTY SEXY"
q
q = sexy_name('WWWWWU')  # "PRETTY SEXY"
q

# 'Very sexy!'
q = sexy_name('YOU')  # 'VERY SEXY'
q
q = sexy_name('FABIO')  # "VERY SEXY"
q
q = sexy_name('ARUUUUUUUUU')  # 'VERY SEXY'
q

# 'The ultimate sexiest!'
q = sexy_name('ROBBY')  # 'THE ULTIMATE SEXIEST'
q
q = sexy_name('SAMANTHA')  # 'THE ULTIMATE SEXIEST'
q
q = sexy_name('DONALD TRUMP')  # "THE ULTIMATE SEXIEST"
q
q = sexy_name('BILL GATES')  # "THE ULTIMATE SEXIEST"
q
q = sexy_name('SCARLETT JOHANSSON')  # "THE ULTIMATE SEXIEST"
q
q = sexy_name('CODEWARS')  # "THE ULTIMATE SEXIEST"
q
q = sexy_name('PAMELA ANDERSON')  # "THE ULTIMATE SEXIEST"
q

# 'Should also handle lowercase letters'
q = sexy_name('you')  # 'VERY SEXY'
q
q = sexy_name('Codewars')  # "THE ULTIMATE SEXIEST"
q
