""" 7kyu - Fun with lists: length

Implement the method length, which accepts a linked list (head), and returns the length of the list.
For example: Given the list: 1 -> 2 -> 3 -> 4, length should return 4.

Note: the list may be null and can hold any type of value. """

# The linked list is defined as follows:

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# def length(head):
#     count = 0
#     while head:
#         head = head.next
#         count += 1
#     return count

def length(head):
    return 1 + length(head.next) if head else 0

q = length(None), 0
q

n1 = Node(1)
n2 = Node(2, n1)
n3 = Node(3, n2)
head = Node(4, n3)
q = length(head), 4
q
