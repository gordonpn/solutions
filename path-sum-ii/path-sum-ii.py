# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        stack = [(root, [root.val], root.val)]
        
        while stack:
            node, nodes_list, path_sum = stack.pop()
            
            if not node.left and not node.right and path_sum == sum:
                result.append(nodes_list)
            
            if node.right:
                stack.append((node.right, nodes_list + [node.right.val], path_sum + node.right.val))
            if node.left:
                stack.append((node.left, nodes_list + [node.left.val], path_sum + node.left.val))
                
        return result
