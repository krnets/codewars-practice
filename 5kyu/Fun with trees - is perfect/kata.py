# from preloaded import TreeNode
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_perfect(tree: TreeNode) -> bool:
    max_depth = 0

    def node_count(node, depth=0):
        nonlocal max_depth
        max_depth = max(max_depth, depth)
        if node is None:
            return 0
        return 1 + node_count(node.left, depth + 1) + node_count(node.right, depth + 1)

    return node_count(tree) == 2**max_depth - 1
