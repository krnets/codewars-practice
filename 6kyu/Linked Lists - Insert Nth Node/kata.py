# class Node(object):
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# def insert_nth(head, index, data):
#     if index == 0:
#         new_node = Node(data)
#         new_node.next = head
#         return new_node

#     sentinel = Node(0)
#     sentinel.next = head
#     prev = sentinel
#     curr = head

#     for _ in range(index):
#         prev = prev.next
#         curr = curr.next

#     new_node = Node(data)
#     new_node.next = curr
#     prev.next = new_node

#     return sentinel.next


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def insert_nth(head, index, data):
    if index == 0:
        return Node(data, head)
    return Node(head.data, insert_nth(head.next, index - 1, data))
