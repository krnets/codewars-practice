from collections import Counter


def longest_palindrome(s):
    freq_values = Counter(filter(str.isalnum, s.lower())).values()
    return sum(v // 2 * 2 for v in freq_values) + any(v % 2 for v in freq_values)
