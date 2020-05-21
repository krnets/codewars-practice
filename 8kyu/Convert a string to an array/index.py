# 8kyu - Convert a string to an array

""" Write a function to split a string and convert it into an array of words. For example:

"Robin Singh" ==> ["Robin", "Singh"]

"I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"] """


def string_to_array(s):
    return s.split(' ')


q = string_to_array("Robin Singh")  # ["Robin", "Singh"]
q
q = string_to_array("CodeWars")  # ["CodeWars"]
q
# ["I", "love", "arrays", "they", "are", "my", "favorite"]
q = string_to_array("I love arrays they are my favorite")
q
q = string_to_array("1 2 3")  # ["1", "2", "3"]
q
q = string_to_array("")  # [""]
q
