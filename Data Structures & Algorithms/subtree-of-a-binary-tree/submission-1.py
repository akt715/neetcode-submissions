# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSame(root,subRoot)-> bool:
            if not subRoot and not root:
                return True
            if not subRoot or not root:
                return False
            
            if root.val != subRoot.val:
                return False
            return isSame(root.left,subRoot.left) and isSame(root.right,subRoot.right)

        def findSubRoot(root, subRoot)->bool:
            if not root:
                return False
            
            if root.val == subRoot.val and isSame(root, subRoot):
                return True
            
            return findSubRoot(root.left, subRoot) or findSubRoot(root.right, subRoot)
        return findSubRoot(root,subRoot)
                    
