# def average_string(s):
#     if not s:
#         return "n/a"
#     tokens, acc = s.split(), 0
#     word_to_int, int_to_word = {}, {}
#     num_words = "zero one two three four five six seven eight nine"

#     for i, w in enumerate(num_words.split()):
#         word_to_int[w] = i
#         int_to_word[i] = w

#     for w in tokens:
#         if w in word_to_int:
#             acc += word_to_int[w]
#         else:
#             return "n/a"
#     return int_to_word[acc // len(tokens)]

words = "zero one two three four five six seven eight nine".split()

def average_string(s):
    try:
        arr = s.split()
        return words[sum(map(words.index, arr)) // len(arr)]
    except:
        return "n/a"
