from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_level_averages(root):
    '''Given a binary tree, populate an array to represent the averages of all of its levels.'''
    res = []
    current_level = 0
    level_size = 0
    queue = deque()
    queue.append(root)
    while queue:
        for _ in range(len(queue)):
            current = queue.popleft()
            current_level += current.val
            level_size += 1

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        res.append(current_level / level_size)
        current_level = 0
        level_size = 0
    return res


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.left.right = TreeNode(2)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
print("Level averages are: " + str(find_level_averages(root)))
