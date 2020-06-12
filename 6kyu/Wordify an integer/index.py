""" 6kyu - Wordify an integer

Turn a given number (an integer > 0, < 1000) into the equivalent English words. 
For the purposes of this kata, no hyphen is needed in numbers 21-99.

Examples:

wordify(1) == "one"
wordify(12) == "twelve"
wordify(17) == "seventeen"
wordify(56) == "fifty six"
wordify(90) == "ninety"
wordify(326) == "three hundred twenty six" """


ONES = 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
TENS = 'zero ten twenty thirty forty fifty sixty seventy eighty ninety'.split()


def wordify(n):
    if n < 20:
        return ONES[n]
    elif n < 100:
        rem = n % 10
        return f"{TENS[n//10]}{' ' + wordify(rem) if rem else ''}"
    elif n < 1000:
        rem = n % 100
        return f"{ONES[n//100]} hundred{' ' + wordify(rem) if rem else ''}"


q = wordify(1), "one"
q
q = wordify(10), "ten"
q
q = wordify(12), "twelve"
q
q = wordify(17), "seventeen"
q
q = wordify(56), "fifty six"
q
q = wordify(90), "ninety"
q
q = wordify(100), "one hundred"
q
q = wordify(326), "three hundred twenty six"
q
q = wordify(770),  'seven hundred seventy'
q
