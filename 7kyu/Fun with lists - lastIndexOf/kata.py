class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def last_index_of(head: Node, search_val: int):
    i = 0
    last_index = -1
    while head:
        if head.data == search_val:
            last_index = i
        i += 1
        head = head.next
    return last_index


def lst_to_link(arr: list) -> Node:
    sentintel = Node(-1)
    curr_node = sentintel
    sentintel.next = curr_node

    for x in arr:
        curr_node.next = Node(x)
        curr_node = curr_node.next

    return sentintel.next
