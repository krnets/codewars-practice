# 6kyu - Counting Duplicates

""" Write a function that will return the count of distinct case-insensitive alphabetic characters 
and numeric digits that occur more than once in the input string. 
The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice """

from collections import Counter

# def duplicate_count(text):
#     freq = Counter(text.lower())
#     return sum(1 for x in freq if freq[x] > 1)

# def duplicate_count(text):
#     freq = Counter(text.lower())
#     return len([x for x in freq if freq[x] > 1])

# def duplicate_count(text):
#     return len([c for c, n in Counter(text.lower()).items() if n > 1])

# def duplicate_count(text):
#     return sum(1 for c, n in Counter(text.lower()).items() if n > 1)

# def duplicate_count(text):
#     return len([c for c in set(text.lower()) if text.lower().count(c) > 1])

def duplicate_count(text):
    return sum(v > 1 for v in Counter(text.lower()).values())


q = duplicate_count("abcde")  # 0
q
q = duplicate_count("abcdea")  # 1
q
q = duplicate_count("aabbcde")  # 2 # 'a' and 'b'
q
q = duplicate_count("aabBcde")
q
#      2 # 'a' occurs twice and 'b' twice (`b` and `B`)
q = duplicate_count("indivisibility")  # 1 # 'i' occurs six times
q
q = duplicate_count("Indivisibilities")
q
#      2 # 'i' occurs seven times and 's' occurs twice
q = duplicate_count("aA11")  # 2 # 'a' and '1'
q
q = duplicate_count("ABBA")  # 2 # 'A' and 'B' each occur twice """
q
