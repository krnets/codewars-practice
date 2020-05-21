# 6kyu - A String of Sorts

""" Define a method that accepts 2 strings as parameters. 
The method returns the first string sorted by the second.

sort_string("foos", "of")       == "oofs"
sort_string("string", "gnirts") == "gnirts"
sort_string("banana", "abn")    == "aaabnn"

To elaborate, the second string defines the ordering. 
It is possible that in the second string characters repeat, 
so you should remove repeating characters, leaving only the first occurrence.

Any character in the first string that does not appear in the second string 
should be sorted to the end of the result in original order. """

# def sort_string(s, ordering):
#     return ''.join(sorted(filter(lambda i: i in ordering, s), key=ordering.index) + [*filter(lambda i: i not in ordering, s)])

def sort_string(s, ordering):
    return ''.join(sorted(s, key=lambda x: list(ordering).index(x) if x in ordering else len(ordering)))


q = sort_string("foos", "of")  # "oofs"
q
q = sort_string("string", "gnirts")  # "gnirts"
q
q = sort_string("banana", "a")  # "aaabnn"
q
