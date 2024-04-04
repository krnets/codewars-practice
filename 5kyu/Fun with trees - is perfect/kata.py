# from preloaded import TreeNode
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# def is_perfect(tree: TreeNode) -> bool:
# # nodes = []
# n = 0
# def dfs(node):
#     nonlocal n
#     # nodes.append(node)
#     # if node.left: dfs(node.left)
#     # if node.right: dfs(node.right)
#     n += 1
#     if node.left is not None: dfs(node.left)
#     if node.right is not None: dfs(node.right)
# dfs(tree)
# # return (len(nodes) - 1).bit_count() == 1
# return (n-1).bit_count() == 1


def is_perfect(tree: TreeNode) -> bool:
    max_depth = 0

    def node_count(node, depth=0):
        nonlocal max_depth
        max_depth = max(max_depth, depth)
        if node is None:
            return 0
        return 1 + node_count(node.left, depth + 1) + node_count(node.right, depth + 1)

    return node_count(tree) == 2**max_depth - 1


# def is_perfect(tree: TreeNode) -> bool:
#     return (count_nodes(tree) + 1).bit_count() == 1

# def count_nodes(node):
#     return 1 + count_nodes(node.left) + count_nodes(node.right) if node else 0
