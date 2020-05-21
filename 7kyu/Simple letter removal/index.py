# 7kyu - Simple letter removal

""" In this Kata, you will be given a lower case string and your task will be to remove 
k characters from that string using the following rule:

- first remove all letter 'a', followed by letter 'b', then 'c', etc...
- remove the leftmost character first.

For example: 
solve('abracadabra', 1) = 'bracadabra' # remove the leftmost 'a'.
solve('abracadabra', 2) = 'brcadabra'  # remove 2 'a' from the left.
solve('abracadabra', 6) = 'rcdbr'      # remove 5 'a', remove 1 'b' 
solve('abracadabra', 8) = 'rdr'
solve('abracadabra',50) = ''           """


# def solve(st, k):
#     chars_to_remove = sorted(st)[0:k]
#     for c in chars_to_remove:
#         st = st.replace(c, '', 1)
#     return st

# def solve(st, k):
#     for c in sorted(st)[0:k]:
#         st = st.replace(c, '', 1)
#     return st

from collections import Counter

def solve(st, k):
    freq = Counter(st)
    uniq = sorted(freq.keys())

    for letter in uniq:
        chars_del = freq[letter] if k >= freq[letter] else k
        st = st.replace(letter, '', chars_del)
        k -= chars_del

    return st


q = solve('abracadabra', 1)  # 'bracadabra'
q
q = solve('abracadabra', 2)  # 'brcadabra'
q
q = solve('abracadabra', 6)  # 'rcdbr'
q
q = solve('abracadabra', 8)  # 'rdr'
q
q = solve('abracadabra', 50)  # ''
q
