class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def linked_list_from_string(s):
    head = Node(-1)
    curr = head
    items = s.split(" -> ")[:-1]

    for v in items:
        new_node = Node(int(v))
        curr.next = new_node
        curr = new_node

    return head.next  # head to linked list
