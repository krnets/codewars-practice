""" 7kyu - Compress sentences

Your task is to make a program takes in a sentence (without puncuation), 
adds all words to a list and returns the sentence as a string which is the 
positions of the word in the list. Casing should not matter too.

"Ask not what your COUNTRY can do for you ASK WHAT YOU CAN DO FOR YOUR country"

becomes

"01234567802856734"

"the one bumble bee one bumble the bee"

becomes

"01231203"  """

# def compress(sentence):
#     words = sentence.lower().split()
#     word_map = {}
#     counter = 0
#     for w in words:
#         if w not in word_map:
#             word_map[w] = counter
#             counter += 1
#     return ''.join(str(word_map[w]) for w in words)

# def compress(sentence):
#     uniq = []
#     words = sentence.lower().split()
#     for w in words:
#         if w not in uniq:
#             uniq.append(w)
#     return ''.join(str(uniq.index(i)) for i in words)

def compress(sentence):
    memo = {}
    return ''.join(str(memo.setdefault(w, len(memo))) for w in sentence.lower().split())


q = compress("The bumble bee"), "012"
q
q = compress("the one bumble bee one bumble the bee"), "01231203"
q
