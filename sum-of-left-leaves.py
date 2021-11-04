# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.processLeft(root, False)
    
    def processLeft(self, root: Optional[TreeNode], isLeft: bool) -> int:
        if not(root):
            return 0
        
        if isLeft and not(root.left) and not(root.right):
            return root.val
        
        return self.processLeft(root.left, True) + self.processLeft(root.right, False)