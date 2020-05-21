# 7kyu - Find the nth occurrence of a word in a string!

""" Implement a function find_nth_occurrence that returns the index of the nth occurrence of 
a substring within a string (considering that those substring could overlap each others). 

If there are less than n occurrences of the substring, return -1.

string = "This is an example. Return the nth occurrence of example in this example string."

find_nth_occurrence("example", string, 1) == 11
find_nth_occurrence("example", string, 2) == 49
find_nth_occurrence("example", string, 3) == 65
find_nth_occurrence("example", string, 4) == -1

Multiple occurrences of a substring are allowed to overlap."""

# def find_nth_occurrence(substring, string, occurrence=1):
#     indices = []
#     pos = 0
#     while(True):
#         pos = string.find(substring, pos)
#         if pos > -1:
#             indices.append(pos)
#             pos += 1
#         else:
#             break
#     return indices[occurrence-1] if occurrence <= len(indices) else -1

import re

# def find_nth_occurrence(substring, string, occurrence=1):
#     matches = list(re.finditer('(?=' + substring + ')', string))
#     return matches[occurrence-1].span()[0] if occurrence <= len(matches) else -1


# def find_nth_occurrence(substring, string, occurrence=1):
#     idx = -1
#     for i in range(occurrence):
#         idx = string.find(substring, idx + 1)
#         if idx == -1:
#             return -1
#     return idx


# def find_nth_occurrence(substring, string, occurrence=1):
#     try:
#         return [s.start() for s in re.finditer('(?=' + substring + ')', string)][occurrence-1]
#     except:
#         return -1

def find_nth_occurrence(substring, string, occurrence=1):
    matches = list(re.finditer('(?=' + substring + ')', string))
    return matches[occurrence-1].start() if occurrence <= len(matches) else -1


string = "This is an example. Return the nth occurrence of example in this example string."


q = find_nth_occurrence("example", string, 1)  # 11
q
q = find_nth_occurrence("example", string, 2)  # 49
q
q = find_nth_occurrence("example", string, 3)  # 65
q
q = find_nth_occurrence("example", string, 4)  # -1
q
q = find_nth_occurrence("TestTest", "TestTestTestTest", 1)  # 0
q
q = find_nth_occurrence("TestTest", "TestTestTestTest", 2)  # 4
q
q = find_nth_occurrence("TestTest", "TestTestTestTest", 3)  # 8
q
q = find_nth_occurrence("TestTest", "TestTestTestTest", 4)  # -1
q
