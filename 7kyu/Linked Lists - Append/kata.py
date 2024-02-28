class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def append(listA, listB):
    if not listA:
        return listB
    curr_node = listA

    while curr_node.next is not None:
        curr_node = curr_node.next

    curr_node.next = listB

    return listA
