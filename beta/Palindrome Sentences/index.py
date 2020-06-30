""" Beta - Palindrome Sentences

Mary brougt home another puzzle book today, and this time it is full of palindrome sentences! 
However, not every phrase is a palindrome, and she needs your help to find all of the actual palindromes.

A word is a palindrome if it is spelt the same when written forwards or backwards. 
A sentence is a palindrome if it is spelt the same forwards or backwards, ignoring all spaces, capitals, and punctuation.

An example of a valid palindrome sentence:

phrase           --> "Was it a cat I saw?"
phrase backwards --> "?was I tac a ti saW"

Notice how, although the phrase and the phrase backwards are not equal strings, the phrase is actually a palindrome.

An example of a fake palindrome sentence:

phrase           --> "Madam, I am Adam."
phrase backwards --> ".madA ma I ,madaM"

Although these strings are similar, the order of their letters is actually slightly different, so it is not a palindrome sentence.

Create a function is_palindrome_sentence that tests if a sentence is a palindrome. 
It takes one input (a string) and returns True or False.

    The punctuation that may appear are: !?.,'/
    The input will always be a string. (No need to test inputs)
    The input could be an empty string: "" """


def is_palindrome_sentence(s):
    s = ''.join(x for x in s.lower() if x.isalpha())
    return s == s[::-1]


q = is_palindrome_sentence("Was it a cat I saw?"), True
q
q = is_palindrome_sentence("Madam, I am Adam."), False
q
q = is_palindrome_sentence(""), True
q
