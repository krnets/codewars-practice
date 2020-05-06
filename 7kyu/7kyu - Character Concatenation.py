# 7kyu - Character Concatenation

""" Given a string, you progressively need to concatenate the first letter from the left 
and the first letter to the right and "1", then the second letter from the left and 
the second letter to the right and "2", and so on.

If the string's length is odd drop the central element.

char_concat("abcdef")    == 'af1be2cd3'
char_concat("abc!def")   == 'af1be2cd3' # same result """

# def char_concat(word):
#     res = ''
#     for i in range(1, len(word)//2+1):
#         res += word[i-1]
#         res += word[-i]
#         res += str(i)
#     return res


# def char_concat(word):
#     res = ''
#     for i in range(1, len(word)//2+1):
#         res += word[i-1] + word[-i] + str(i)
#     return res

def char_concat(word):
    return ''.join('{}{}{}'.format(word[i], word[-i-1], i+1) for i in range(len(word)//2))


q = char_concat("abc def"), 'af1be2cd3'
q
q = char_concat("CodeWars"), 'Cs1or2da3eW4'
q
