class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# clever way to add numbers together without changing to string
# otherwise just another example of how to return your recursive the way you want

def find_sum_of_path_numbers(root: TreeNode) -> int:
    '''Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number. Find the total sum of all the numbers represented by all paths.'''

    return find_root_to_leaf_path_numbers(root, 0)


def find_root_to_leaf_path_numbers(currentNode, pathSum):
    if currentNode is None:
        return 0

    # calculate the path number of the current node
    pathSum = 10 * pathSum + currentNode.val

    # if the current node is a leaf, return the current path sum
    if currentNode.left is None and currentNode.right is None:
        return pathSum

    # traverse the left and the right sub-tree
    return find_root_to_leaf_path_numbers(currentNode.left, pathSum) + find_root_to_leaf_path_numbers(currentNode.right, pathSum)

# works the same:
    return dfs(root, '', 0)

# def dfs(node: TreeNode, current_number: str, total: int):
#     if node is None:
#         return 0
#     current_number += str(node.val)
#     if node.left is None and node.right is None:
#         total += int(current_number)
#         return total
#     return dfs(node.left, current_number, total) + dfs(node.right, current_number, total)


root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.right.left = TreeNode(6)
root.right.right = TreeNode(5)
print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))
