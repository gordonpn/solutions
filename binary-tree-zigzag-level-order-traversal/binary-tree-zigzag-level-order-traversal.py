# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        results = []
        queue = []
        
        if root:
            queue.append(root)
            
        alternate = 1
        
        while queue:
            level = []
            size = len(queue)
            
            for _ in range(size):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            level = level[::alternate]
            alternate *= -1
            results.append(level)
            
        return results
