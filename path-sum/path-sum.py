# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        stack = [(root, root.val)]

        while stack:
            node, path_sum = stack.pop()

            if not node.left and not node.right and path_sum == sum:
                return True
            if node.left:
                stack.append((node.left, path_sum + node.left.val))
            if node.right:
                stack.append((node.right, path_sum + node.right.val))

        return False
