# 5kyu - Simple Pig Latin

""" Move the first letter of each word to the end of it, then add "ay" to the end of the word. 
Leave punctuation marks untouched. """

# def pig_it(text):
#     return ' '.join(word[1:] + word[0] + 'ay' if word.isalpha() else word for word in text.split())

import re

def pig_it(text):
    return re.sub(r'([\w])([\w]*)', r'\2\1ay', text)


q = pig_it('Pig latin is cool')  # igPay atinlay siay oolcay
q
q = pig_it('Hello world !')     # elloHay orldway !
q
q = pig_it('Pig latin is cool')
# 'igPay atinlay siay oolcay'
q
q = pig_it('This is my string')
# 'hisTay siay ymay tringsay'
q
