class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def length(node):
    res = 0
    while node:
        res += 1
        node = node.next
    return res


def count(node, data):
    res = 0
    while node:
        if node.data == data:
            res += 1
        node = node.next
    return res
