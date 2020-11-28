# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        result = []
        queue = [root]
        
        while queue:
            temp = queue.pop()
            result.append(temp.val)
            
            if temp.right:
                queue.append(temp.right)
            if temp.left:
                queue.append(temp.left)
            
        return result
        
