# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        result = []
        stack = [root]

        while stack:
            temp = stack.pop()
            result.append(temp.val)

            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)

        return result
