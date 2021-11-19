# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def traverse(depth: int, node: Optional[TreeNode]) -> int:
            if not(node):
                return depth
            return max(traverse(depth + 1, node.left), traverse(depth + 1, node.right))
        
        return traverse(0, root)