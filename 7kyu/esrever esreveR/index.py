# 7kyu - esrever esreveR!

""" In this kata you must take an input string, reverse the order of the words, 
and reverse the order of the letters within the words.

But, as a bonus, every test input will end with a punctuation mark (! ? .) 
and the output should be returned with the mark at the end.

A few examples should help clarify:

esrever("hello world.") == "dlrow olleh."
esrever("Much l33t?") == "t33l hcuM?"
esrever("tacocat!") == "tacocat!"

Quick Note: A string will always be passed in (though it may be empty) so no need for error-checking other types. """


def esrever(string):
    return string[::-1][1:] + string[-1:]

# def esrever(string):
#     return string[:-1][::-1] + string[-1] if string else ''


q = esrever('an Easy one?')  # 'eno ysaE na?'
q
q = esrever('a small lOan OF 1,000,000 $!')  # '$ 000,000,1 FO naOl llams a!'
q
q = esrever('<?> &!.".')  # '".!& >?<.'
q
q = esrever('b3tTer p4ss thIS 0ne.')  # 'en0 SIht ss4p reTt3b.'
q
q = esrever('')  # ''
q
