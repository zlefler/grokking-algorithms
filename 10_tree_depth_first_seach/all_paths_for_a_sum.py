class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

# need an array of current path and finished paths.
# IMPORTANT: You don't need to return anything from the dfs, so you can make
# an array, then after the recursive call you can delete from it to keep the
# array right for the current iteration. You can't do this if you have to return
# your recursive call.
# BUT! If you do this, you need to make a COPY of the array to push to the result
# array. Otherwise as you backtrack, the result array will also disappear.


def find_paths(root: TreeNode, sum: int) -> list[int]:
    '''Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.'''

    all_paths = []
    dfs(root, sum, [], all_paths)
    return all_paths


def dfs(node: TreeNode, sum: int, current_path: list[int], all_paths: list[list]):
    if node == None:
        return
    current_path.append(node.val)
    if node.val == sum and node.left is None and node.right is None:
        all_paths.append(list(current_path))
    else:
        dfs(node.left, sum - node.val, current_path, all_paths)
        dfs(node.right, sum - node.val, current_path, all_paths)

    current_path.pop()


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
required_sum = 23
print("Tree paths with required_sum " + str(required_sum) +
      ": " + str(find_paths(root, required_sum)))
