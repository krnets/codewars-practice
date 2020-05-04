# 7kyu - Arithmetic List!

""" In this kata, you will write an arithmetic list which is basically a list that contains consecutive terms in the sequence.
You will be given three parameters :

    `first` the first term in the sequence
    `c` the constant that you are going to ADD ( since it is an arithmetic sequence...)
    `l` the number of terms that should be `return`ed

Don't forget about the indexing pitfall """


def seqlist(first, c, l):
    return list(range(first, first + c * l, c))


q = seqlist(0, 1, 20)  # [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
q
