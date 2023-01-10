from ctypes.wintypes import tagMSG


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

# If you need to be able to evaluate every possible combo, you can hold an array with all the nodes
# and iterate through it backwards to try them out.


def count_paths(root: TreeNode, sum: int) -> int:
    '''Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of all the node values of each path equals ‘S’. Please note that the paths can start or end at any node but all paths must follow direction from parent to child (top to bottom).'''

    return dfs(root, sum, [])


def dfs(node, target_sum, current_path):
    if node is None:
        return 0

    current_path.append(node.val)
    valid_paths, sum = 0, 0

    for i in range(len(current_path)-1, -1, -1):
        sum += current_path[i]
        if sum == target_sum:
            valid_paths += 1

    valid_paths += dfs(node.left, target_sum, current_path)
    valid_paths += dfs(node.right, target_sum, current_path)

    current_path = current_path[:-1]

    return valid_paths


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
print("Tree has paths: " + str(count_paths(root, 11)))
