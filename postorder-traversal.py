# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traversal(root: Optional[TreeNode], arr:List[int]):
            if root:
                traversal(root.left, arr)
                traversal(root.right, arr)
                arr.append(root.val)
        arr = []
        traversal(root, arr)
        return arr