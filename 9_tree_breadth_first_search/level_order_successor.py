from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_successor(root, key):

    queue = deque()
    queue.append(root)
    while queue:
        curr = queue.popleft()
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
        if curr.val == key:
            return queue[0]
    return None


# it works fine, but is more complicated than it needs to be:
    # queue = deque()
    # queue.append(root)
    # nodes = []
    # while queue:
    #     for _ in range(len(queue)):
    #         curr = queue.popleft()
    #         nodes.append(curr)
    #         if curr.left:
    #             queue.append(curr.left)
    #         if curr.right:
    #             queue.append(curr.right)

    # for i in range(len(nodes)):
    #     if nodes[i].val == key:
    #         return nodes[i+1]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

result = find_successor(root, 3)
if result:
    print(result.val)

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

result = find_successor(root, 9)
if result:
    print(result.val)

result = find_successor(root, 12)
if result:
    print(result.val)
