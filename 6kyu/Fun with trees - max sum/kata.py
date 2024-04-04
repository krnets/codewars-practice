# from preloaded import TreeNode


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def max_sum(root: TreeNode) -> int:
    if not root:
        return 0
    if not root.left:
        return root.value + max_sum(root.right)
    if not root.right:
        return root.value + max_sum(root.left)
    return root.value + max(max_sum(root.left), max_sum(root.right))
