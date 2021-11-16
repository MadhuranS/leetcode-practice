# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(root: Optional[TreeNode], arr: List[int]):
            if root.left:
                arr.append(root.left.val)
                traverse(root.left, arr)
            if root.right:
                arr.append(root.right.val)
                traverse(root.right, arr)
        arr = []
        if not root:
            return arr
        arr.append(root.val)
        traverse(root, arr)
        return arr