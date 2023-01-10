from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_min_depth(root):
    '''Find the minimum depth of a binary tree. The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.'''
    queue = deque()
    queue.append(root)
    current_level = 0
    while queue:
        current_level += 1
        for _ in range(len(queue)):
            curr = queue.popleft()
            if not curr.left and not curr.right:
                return current_level
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
    return current_level


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
print("Tree Minimum Depth: " + str(find_min_depth(root)))
root.left.left = TreeNode(9)
root.right.left.left = TreeNode(11)
print("Tree Minimum Depth: " + str(find_min_depth(root)))
