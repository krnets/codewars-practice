# 7kyu - Complementary DNA

""" Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" 
for the development and functioning of living organisms.

If you want to know more http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". 
You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. 
DNA strand is never empty or there is no DNA at all (again, except for Haskell).

More similar exercise are found here http://rosalind.info/problems/list-view/ (source)

DNA_strand ("ATTGC") # return "TAACG"
DNA_strand ("GTAT") # return "CATA" """


# def DNA_strand(dna):
#     complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
#     return ''.join(complement[c] for c in dna)


def DNA_strand(dna):
    return dna.translate(str.maketrans("ACGT", "TGCA"))


q = DNA_strand("AAAA")  # "TTTT","String AAAA is"
q
q = DNA_strand("ATTGC")  # "TAACG","String ATTGC is"
q
q = DNA_strand("GTAT")  # "CATA","String GTAT is"
q
