from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None


def connect_level_order_siblings(root):
    '''Given a binary tree, connect each node with its level order successor. The last node of each level should point to a null node.'''
    queue = deque()
    queue.append(root)

    while queue:
        previous_node = None
        level_size = len(queue)
        for _ in range(level_size):
            current = queue.popleft()
            if previous_node:
                previous_node.next = current
                previous_node = current
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
    return root


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
connect_level_order_siblings(root)

print("Level order traversal using 'next' pointer: ")
root.print_level_order()
