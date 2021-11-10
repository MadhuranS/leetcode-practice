# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root1 and not root2:
            return None

        if root1 and root2:
            newroot = TreeNode(root1.val + root2.val)
            newroot.left = self.mergeTrees(root1.left, root2.left)
            newroot.right = self.mergeTrees(root1.right, root2.right)
            return newroot

        elif not(root1):
            newroot = TreeNode(root2.val)
            newroot.left = self.mergeTrees(None, root2.left)
            newroot.right = self.mergeTrees(None, root2.right)
            return newroot

        elif not(root2):
            newroot = TreeNode(root1.val)
            newroot.left = self.mergeTrees(root1.left, None)
            newroot.right = self.mergeTrees(root1.right, None)
            return newroot
        