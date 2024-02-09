# def longest_palindrome(s):
#     if not s:
#         return 0
#     longest = 0
#     for i in range(len(s)):
#         even_pali = expand_from_middle(s, i, i)
#         odd_pali = expand_from_middle(s, i, i + 1)
#         longest = max(longest, even_pali, odd_pali)
#     return longest - 1


# def expand_from_middle(s, left, right):
#     while left >= 0 and right < len(s) and s[left] == s[right]:
#         left -= 1
#         right += 1
#     return right - left


def longest_palindrome(s):
    if not s:
        return 0
    longest = 1
    for i in range(len(s)):
        even_pali = expand_from_middle(s, i, i + 1)
        odd_pali = expand_from_middle(s, i, i)
        longest = max(longest, even_pali, odd_pali)
    return longest


def expand_from_middle(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1
