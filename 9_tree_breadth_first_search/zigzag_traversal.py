from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    '''Given a binary tree, populate an array to represent its zigzag level order traversal. You should populate the values of all nodes of the first level from left to right, then right to left for the next level and keep alternating in the same manner for the following levels.'''

    result = []
    if root is None:
        return result

    queue = deque()
    queue.append(root)
    leftToRight = True
    while queue:
        level_size = len(queue)
        current_level = deque()
        for _ in range(level_size):
            current = queue.popleft()

            if leftToRight:
                current_level.append(current.val)
            else:
                current_level.appendleft(current.val)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        result.append(list(current_level))
        leftToRight = not leftToRight
    return result


# doesn't work:
#     res = deque()
#     if root is None:
#         return res
#     queue = deque()
#     queue.append(root)
#     while queue:
#         i = 0
#         current_level = []
#         level_size = len(queue)
#         for _ in range(level_size):

#             if i % 2 == 0:
#                 current = queue.popleft()
#                 current_level.append(current.val)
#                 if current.right:
#                     queue.append(current.right)
#                 if current.left:
#                     queue.append(current.left)
#             else:
#                 current = queue.pop()
#                 current_level.append(current.val)
#                 if current.left:
#                     queue.append(current.left)
#                 if current.right:
#                     queue.append(current.right)
#         res.append(current_level)

#     return res


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
root.right.left.left = TreeNode(20)
root.right.left.right = TreeNode(17)
print("Zigzag traversal: " + str(traverse(root)))
