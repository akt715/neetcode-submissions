# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [float('-inf')]
        self.helper(root,res)
        return res[0]
    def helper(self,root, res):
        if not root: 
            return 0

        left = self.helper(root.left,res)
        right = self.helper(root.right,res)
        left = max(left,0)
        right = max(right,0)
        res[0] = max(res[0],root.val + left+right)

        return root.val + max(left,right)