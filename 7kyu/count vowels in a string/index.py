# 7kyu - count vowels in a string

""" Write a function count_vowels to count the number of vowels in a given string.

    Return nil or None for non-string inputs.
    Return 0 if the parameter is omitted.

count_vowels("abcdefg") => 2
count_vowels("aAbcdeEfg") => 4
count_vowels(12) => None """


# def count_vowels(s=''):
#     return sum(1 for c in s if c in 'aeiouAEIOU') if isinstance(s, str) else None

def count_vowels(s=''):
    return sum(1 for c in s.lower() if c in 'aeiou') if isinstance(s, str) else None


q = count_vowels("abcdefg")  # 2
q
q = count_vowels("asdfdsafdsafds")  # 3
q
