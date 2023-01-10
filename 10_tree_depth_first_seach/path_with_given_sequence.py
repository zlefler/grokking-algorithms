class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

# if need to match with an array, much easier to use an index than to create a list to compare.
# That way, you don't have to go backwards and delete off the list.


def find_path(root: TreeNode, sequence: list):
    '''Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.'''

    return dfs(root, sequence, 0)


def dfs(node, sequence, index):
    if node is None:
        return False
    if node.val == sequence[index] and node.left is None and node.right is None:
        return True
    return dfs(node.left, sequence, index + 1) or dfs(node.right, sequence, index + 1)


root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.right.left = TreeNode(6)
root.right.right = TreeNode(5)

print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))
