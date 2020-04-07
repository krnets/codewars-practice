# 8kyu - Reversing Words in a String

""" Write a function that reverses the words in a given string. 
A word can also fit an empty string. If this is not clear enough, here are some examples:

As the input may have trailing spaces, you will also need to ignore unneccesary whitespace. """


def reverse(st):
    return ' '.join(reversed(st.split()))


q = reverse('Hello World')  # 'World Hello'
q
q = reverse('Hi There.')  # 'There. Hi'
q
