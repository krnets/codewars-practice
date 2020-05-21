# 7kyu - Convert a linked list to a string

""" Preloaded for you is a class, struct or derived data type Node used to construct linked lists in this Kata.

Create a function stringify which accepts an argument list/$list and returns a string 
representation of the list. The string representation of the list starts with the value 
of the current Node, specified by its data/$data/Data property, followed by a whitespace 
character, an arrow and another whitespace character (" -> "), followed by the rest of the list. 
The end of the string representation of a list must always end with null/NULL/None/nil/nullptr/null() 
(all caps or all lowercase depending on the language you are undertaking this Kata in). 
For example, given the following list:

Node(1, Node(2, Node(3)))

... its string representation would be:

"1 -> 2 -> 3 -> None"

And given the following linked list:

Node(0, Node(1, Node(4, Node(9, Node(16)))))

... its string representation would be:

"0 -> 1 -> 4 -> 9 -> 16 -> None"

Note that None itself is also considered a valid linked list. 
In that case, its string representation would simply be "None".

For the simplicity of this Kata, you may assume that any Node in this Kata may only contain 
non-negative integer values. For example, you will not encounter a Node whose data property is "Hello World". """


class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# def stringify(node):
#     if not node:
#         return 'None'
#     res = [node.data]
#     while node.next:
#         node = node.next
#         res.append(node.data)
#     res.append(None)
#     return ' -> '.join(str(x) for x in res)

# def stringify(node):
#     if not node:
#         return 'None'
#     return str(node.data) + ' -> ' + stringify(node.next)


def stringify(node):
    return '{} -> {}'.format(str(node.data), stringify(node.next)) if node else 'None'


q = stringify(Node(0, Node(1, Node(2, Node(3)))))  # '0 -> 1 -> 2 -> 3 -> None'
q
# q = stringify(None)  # 'None'
# q
# '0 -> 1 -> 4 -> 9 -> 16 -> None'
q = stringify(Node(0, Node(1, Node(4, Node(9, Node(16))))))
q
