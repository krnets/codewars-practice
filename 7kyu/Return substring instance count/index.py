# 7kyu - Return substring instance count

""" Complete the solution so that it returns the number of times the search_text is found within the full_text.

Usage example:

solution('aa_bb_cc_dd_bb_e', 'bb') # should return 2 since bb shows up twice
solution('aaabbbcccc', 'bbb') # should return 1 """


# def solution(full_text, search_text):
#     return full_text.count(search_text)

solution = str.count

q = solution('abcdeb', 'b')  # 2
q
q = solution('abc', 'b')  # 1
q
q = solution('abbc', 'bb')  # 1
q
