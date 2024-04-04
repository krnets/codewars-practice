# from preloaded import Node


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.value}"

    def __repr__(self):
        return str(self)


# def array_to_tree(arr):
#     if not arr:
#         return None
#     nodes_arr = [Node(x) for x in arr]

#     for i in range(n := len(nodes_arr)):
#         if 2 * i + 1 < n:
#             nodes_arr[i].left = nodes_arr[2 * i + 1]
#         if 2 * i + 2 < n:
#             nodes_arr[i].right = nodes_arr[2 * i + 2]

#     return nodes_arr[0]


def array_to_tree(arr, index=0):
    if index < len(arr):
        return Node(
            arr[index],
            array_to_tree(arr, 2 * index + 1),
            array_to_tree(arr, 2 * index + 2),
        )
