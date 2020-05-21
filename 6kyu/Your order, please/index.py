# 6kyu - Your order, please

""" Your task is to sort a given string. Each word in the string will contain a single number. 
This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. 
The words in the input String will only contain valid consecutive numbers.

"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""          """

# import re

# def order(sentence):
#     words = (sentence.split())
#     tup = zip(words, words)
#     res = [[int(re.sub(r'\D', '', t[0])), t[1]] for t in tup]
#     return ' '.join(x[1] for x in sorted(res))

# def order(sentence):
#     return ' '.join(sorted(sentence.split(), key=lambda x: sorted(x)))

# def order(sentence):
#     return ' '.join(sorted(sentence.split(), key=sorted))

def order(sentence):
    return ' '.join(sorted(sentence.split(), key=min))


q = order("is2 Thi1s T4est 3a")  # "Thi1s is2 3a T4est"
q
# "Fo1r the2 g3ood 4of th5e pe6ople"
q = order("4of Fo1r pe6ople g3ood th5e the2")
q
q = order("")  # ""
q
