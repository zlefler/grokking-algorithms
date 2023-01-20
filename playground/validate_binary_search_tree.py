class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root) -> bool:
    def is_valid(node, parent, left):
        if not node:
            return True
        if left:
            if node.val >= parent:
                return False
        else:
            if node.val <= parent:
                return False
        return is_valid(node.left, node.val, True) and is_valid(node.right, node.val, False)

    return is_valid(root, -1, False)


node = TreeNode(5)
node.left = TreeNode(4)
node.right = TreeNode(6)
node.right.left = TreeNode(3)
node.right.right = TreeNode(7)

print(isValidBST(node))
