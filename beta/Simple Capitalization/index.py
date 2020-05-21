# Beta - Simple Capitalization

""" Define three functions:

    capitalize_string -> with first letter capitalized and all other letters lowercased;
    capitalize_words -> with the first letter of every word capitalized and all other letters lowercased.
    capitalize_sentences -> with the first letter of every sentence capitalized and all other letters lowercased. 

    Here we consider each sentence to be ended by a period, a question-mark or an exclamation mark, 
    and we consider a new sentence to begin with the first non-whitespace character 
    (including newlines as whitespace). """


def capitalize_string(s):
    return s.capitalize()

def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

def capitalize_sentences(s):
    return ''.join(c.upper() if i > 1 and s[i - 2] in '.!?' else c for i, c in enumerate(s.capitalize()))


q = capitalize_string("This is a test. This is only a test.")
q
# 'This is a test. this is only a test.'

q = capitalize_words("This is a test. This is only a test.")
q
# 'This Is A Test. This Is Only A Test.'

q = capitalize_sentences("This is a test. This is only a test.")
q
# 'This is a test. This is only a test.'
