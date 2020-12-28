# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        result = []
        if not root:
            return result
        
        stack = [(root, str(root.val))]
        
        while stack:
            node, nodes_list = stack.pop()
            
            if not node.left and not node.right:
                result.append(nodes_list)
                
            if node.right:
                right_nodes_list = nodes_list + "->" + str(node.right.val)
                stack.append((node.right, right_nodes_list))
            if node.left:
                left_nodes_list = nodes_list + "->" + str(node.left.val)
                stack.append((node.left, left_nodes_list))
                
        return result